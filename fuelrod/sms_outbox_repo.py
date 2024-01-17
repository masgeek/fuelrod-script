import string
from my_logger import MyLogger
from orm.database_conn import MyDb
from sqlalchemy.orm import sessionmaker
from orm.fuelrod import SmsOutbox


class SmsOutBoxRepo:
    def __init__(self):
        self.db_engine = MyDb()
        self.session = sessionmaker(bind=self.db_engine)
        self.logging = MyLogger()

    def load_messages(self, limit: int = 100):
        return self.session().query(SmsOutbox).limit(limit).all()
