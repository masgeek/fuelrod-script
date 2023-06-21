import concurrent.futures
import json
from os import environ

from dotenv import load_dotenv

from fee import fee_payment
from fuelrod.fuelrod_api import SmsUser
from fuelrod.sms_notification import SmsNotification
from my_logger import MyLogger

load_dotenv(verbose=True)
fuelrod_base_url = environ.get("SMS_BASE_URL")
api_username = environ.get("SMS_API_USER")
api_pass = environ.get("SMS_API_PASS")

fee_api_user = environ.get("FEE_API_USER")
fee_api_pass = environ.get("FEE_API_PASS")
log_level = environ.get("LOG_LEVEL", "INFO")
debug_db = environ.get("DEBUG_DB", False)

logging = MyLogger()

apiUser = SmsUser()
feeProcessing = fee_payment.FeePayment(
    api_user=fee_api_user, api_pass=fee_api_pass, my_logger=logging
)

token = apiUser.auth_token(username=api_username, password=api_pass)

fee_endpoints = apiUser.fee_endpoints(token=token)

smsNotification = SmsNotification(base_url=fuelrod_base_url, token=token)


def process_sms_notifications(username, end_point, page_size, page_no=1):
    logging.info(f"processing data for {username} for page number {page_no}")
    yield feeProcessing.process_notifications(
        username=username, endpoint=end_point, page_size=page_size, page_number=page_no
    )


def update_sent_message(sms_future):
    sms = sms_future.result()
    print(json.dumps(sms, indent=4))
    update_resp = feeProcessing.update_sms_notification(
        message_id=sms["id"], username=sms["username"], endpoint=sms["endpoint"]
    )
    logging.debug(next(update_resp))


if __name__ == "__main__":
    for fee_endpoint in fee_endpoints:
        __username = fee_endpoint["username"]
        __end_point = fee_endpoint["endpoint"]
        all_results = []
        sent_messages = []
        _page_number = 1
        _page_size = 250
        _results = feeProcessing.process_notifications(
            username=__username, endpoint=__end_point, page_size=_page_size
        )
        resp_value = next(_results)
        last_page = resp_value["last_page"]
        # print(json.dumps(resp_value['links'], indent=4))
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {
                executor.submit(
                    process_sms_notifications,
                    __username,
                    __end_point,
                    _page_size,
                    _page_number,
                )
                for _page_number in range(1, last_page + 1)
            }
            for future in concurrent.futures.as_completed(futures):
                try:
                    results = future.result()
                    resp_val = next(next(results))
                    next_page_url = resp_val["next_page_url"]
                    all_results.extend(resp_val["data"])
                    logging.debug(f"Last page number {next_page_url}")
                except Exception as exc:
                    logging.error(f"Exception: {exc}", exc_info=True)

        logging.info(f"Size of results is {len(all_results)}")

        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Process each item in the dictionary asynchronously and send the result to the REST API
            for message in all_results:
                sent_messages.append(
                    {
                        "endpoint": __end_point,
                        "username": __username,
                        "id": message["id"],
                    }
                )

                _result = executor.submit(
                    smsNotification.send_sms, message, __end_point
                )
                _result.add_done_callback(update_sent_message)
