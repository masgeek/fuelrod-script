import json
from os import environ

from dotenv import load_dotenv

from fuelrod.campaign_repo import CampaignRepo
from fuelrod.fuelrod_api import MessageStatus, SmsUser
from fuelrod.user_repo import UserRepo
from my_logger import MyLogger

load_dotenv(verbose=True)
log_level = environ.get("LOG_LEVEL", "INFO")
api_username = environ.get("SMS_API_USER")
api_pass = environ.get("SMS_API_PASS")

logging = MyLogger()

apiUser = SmsUser()
token = apiUser.auth_token(username=api_username, password=api_pass)
campaignRepo = CampaignRepo(fuelrod_token=token)
userRepo = UserRepo()
campaigns = campaignRepo.load_unprocessed_campaigns(
    campaign_status=MessageStatus.IN_PROGRESS, limit=50
)

total_campaigns = len(campaigns)
if total_campaigns <= 0:
    logging.info("No pending campaign(s)")
else:
    logging.info(f"Processing {total_campaigns} campaign(s)")
    for campaign in campaigns:
        user = userRepo.load_user(campaign.user_uuid)
        if user is not None and user.flag_reason == MessageStatus.ACTIVE.name:
            logging.info(f"Processing message for {user.client_name}")
            creditInfo = apiUser.credit_info(user_uuid=user.uuid, token=token)
            logging.debug(f"The credit info is \n{json.dumps(creditInfo, indent=4)}")

            if "status" in creditInfo:
                status_string = creditInfo["status"]
                status_enum = MessageStatus.__getitem__(status_string)
                campaignRepo.update_campaign(campaign.id, status_enum)

                if creditInfo["canSend"]:
                    logging.info(
                        f"Processing campaign `{campaign.campaign_name.upper()}`"
                    )
                    campaignRepo.process_queue(
                        campaign_id=campaign.id, username=user.username
                    )
                else:
                    logging.warning(
                        "Cannot process this campaign due to insufficient credits"
                    )
