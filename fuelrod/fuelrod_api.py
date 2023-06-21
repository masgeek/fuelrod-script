import enum
import json
from calendar import timegm
from datetime import datetime
from os import environ

import requests
from cachetools import cached, TTLCache
from dotenv import load_dotenv
from requests import HTTPError

from my_logger import MyLogger

cache = TTLCache(maxsize=100, ttl=86400)

load_dotenv(verbose=True)
fuelrod_base_url = environ.get("SMS_BASE_URL")


class MessageStatus(enum.Enum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    MESSAGE_SENT = "MESSAGE_SENT"
    PAUSED_NO_CREDIT = "PAUSED_NO_CREDIT"
    UNPAID_INVOICES = "UNPAID_INVOICES"
    ACTIVE = "ACTIVE"
    DUPLICATE_MESSAGE = "DUPLICATE_MESSAGE"
    PAUSED = "PAUSED"
    INSUFFICIENT_CREDITS = "INSUFFICIENT_CREDITS"
    STATUS_PENDING = "STATUS_PENDING"
    SUCCESS = "SUCCESS"
    USER_OPTED_OUT = "USER_OPTED_OUT"


class SmsUser:
    def __init__(self):
        self.base_url = fuelrod_base_url
        self.logging = MyLogger()

    def fee_endpoints(self, token):
        _url = self.base_url + "/v1/fee-endpoints"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        try:
            with requests.session() as session:
                _response = session.get(url=_url, headers=headers)
                _response.raise_for_status()
                resp = _response.json()
                return resp["content"]
        except HTTPError as http_err:
            self.logging.error(f"Unable to fetch fee endpoints -> {http_err}")
        except Exception as err:
            self.logging.error(f"Other error occurred -> {err}")

    def credit_info(self, user_uuid, token):
        _url = self.base_url + f"/v1/credit/user/{user_uuid}/summary"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        credit_info = {
            "canSend": False,
            "smsLeft": 0,
            # "status": MessageStatus.PAUSED.name,
        }
        try:
            with requests.session() as session:
                _response = session.get(url=_url, headers=headers)
                _response.raise_for_status()
                resp = _response.json()

                overdraft_enabled = resp["overdraft"]
                sms_left = resp["smsLeft"]

                can_send = sms_left > 5 or overdraft_enabled
                credit_info = {
                    "canSend": can_send,
                    "overdraft": resp["overdraft"],
                    "smsLeft": 1000 if overdraft_enabled else sms_left,
                    "status": MessageStatus.IN_PROGRESS.name
                    if can_send
                    else MessageStatus.PAUSED_NO_CREDIT.name,
                    "smsCost": resp["cost"],
                    "creditLeft": resp["creditLeft"],
                }
        except HTTPError as http_err:
            self.logging.error(f"Unable to fetch credit info -> {http_err}")
        except Exception as err:
            self.logging.error(f"Other error occurred -> {err}")

        return credit_info

    @cached(cache=cache)
    def auth_token(self, username, password):
        self.logging.info(f"Authenticating user {username}")
        _url = self.base_url + "/v1/account/auth"

        payload = {"username": username, "password": password}
        token = self._read_token_file()
        if token is not None:
            self.logging.debug("Found token in file using it instead of refreshing")
            return token
        try:
            self.logging.debug("Fetching new token from aPI")
            _response = requests.post(url=_url, json=payload)
            _response.raise_for_status()
            resp = _response.json()
            with open("token/fuelrod-token.json", "w") as json_file_obj:
                json.dump(resp, json_file_obj, indent=4)

            token = resp["accessToken"]
        except HTTPError as http_err:
            self.logging.error(f"Unable to authenticate user {http_err}")
        except Exception as err:
            self.logging.error(f"Other error occurred {err}")

        return token

    def _read_token_file(self):
        token_json_file = "token/fuelrod-token.json"
        token = None
        try:
            with open(token_json_file, "r") as json_file_obj:
                token_data = json.load(json_file_obj)
                current_time = timegm((datetime.utcnow().utctimetuple()))
                expiry_time = 0
                if "accessToken" in token_data:
                    token = token_data["accessToken"]
                    expiry_time = token_data["expiry"]
                token_expired = current_time > expiry_time
                if token_expired:
                    token = None
                    self.logging.info(f"Token has expired at {expiry_time}")

        except Exception as err:
            self.logging.critical(f"Error reading {token_json_file} file {err}")

        return token


class MessagingService:
    def __init__(self, token):
        self.base_url = fuelrod_base_url
        self.token = token
        self.logging = MyLogger()

    def send_campaign(self, campaigns):
        _url = f"{self.base_url}/v1/campaign/send-message/{campaigns['username']}"

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}",
        }

        self.logging.debug(f"Message payload is \n{json.dumps(campaigns, indent=4)}")
        try:
            with requests.session() as session:
                _response = session.post(url=_url, json=campaigns, headers=headers)
                _response.raise_for_status()
                resp = _response.json()
                resp["record_id"] = campaigns["id"]

                self.logging.debug(
                    f"Message payload response \n{json.dumps(resp, indent=4)}"
                )
                return resp

        except HTTPError as http_err:
            self.logging.error(
                f"Unable send campaign message -> {http_err.response} : {http_err.response.text}"
            )
        except Exception as err:
            self.logging.critical(f"Other error occurred -> {err}")
