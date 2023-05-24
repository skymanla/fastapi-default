from pydantic import BaseSettings


class DBSetting(BaseSettings):
    DB_HOST = ""
    DB_NAME = ""
    DB_USER = ""
    DB_PWD = ""
    DB_PORT = ""

    class Config:
        env_file = "app/.env"
