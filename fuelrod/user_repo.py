import string

from sqlalchemy.orm import sessionmaker

from my_logger import MyLogger
from orm.database_conn import MyDb
from orm.fuelrod import Users


class UserRepo:
    def __init__(self):
        self.db_engine = MyDb()
        self.session = sessionmaker(bind=self.db_engine)
        self.logging = MyLogger()

    def load_user(self, user_uuid: string) -> Users | None:
        return self.session().query(Users).filter(Users.uuid == user_uuid).first()
