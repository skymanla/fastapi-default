import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import DBSetting

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))


class DBConn:
    def __init__(self):
        _DBSettings = DBSetting()
        _user = _DBSettings.DB_USER
        _password = _DBSettings.DB_PWD
        _host = _DBSettings.DB_HOST
        _port = _DBSettings.DB_PORT
        _dbname = _DBSettings.DB_NAME

        self.engine = create_engine("mysql+pymysql://"
                                    + str(_user)
                                    + ":"
                                    + str(_password)
                                    + "@"
                                    + str(_host)
                                    + ":"
                                    + str(_port)
                                    + "/"
                                    + str(_dbname), pool_recycle=500
                                    )

    def session_maker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def connection(self):
        conn = self.engine.connect()
        try:
            return conn
        finally:
            conn.close()

    def get_engine(self):
        return self.engine
