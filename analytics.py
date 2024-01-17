from fuelrod.sms_outbox_repo import SmsOutBoxRepo
from my_logger import MyLogger

logging = MyLogger()

outbox = SmsOutBoxRepo()

messages = outbox.load_messages()

logging.info(f"Messages loaded: {len(messages)}")
