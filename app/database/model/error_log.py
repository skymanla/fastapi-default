from sqlalchemy import Column, String, Integer, BigInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ErrorLog(Base):
    __tablename__ = 'error_log'
    __table_args__ = {'comment': 'error log'}
    idx = Column(BigInteger, primary_key=True, autoincrement=True, comment='pk')
    clientIp = Column(String, nullable=False, index=True, name='client_ip', comment='client ip')
    errorUrl = Column(String, nullable=False, index=True, name='error_url', comment='error url')
    statusCode = Column(Integer, nullable=False, name='status_code', comment='http status code')
    errorPayload = Column(String, nullable=True, name='error_payload', comment='error payload')
    errorMessage = Column(String, nullable=True, name='error_message', comment='error message')

    def __init__(self, clientIp, errorUrl, statusCode, errorPayload, errorMessage):
        self.clientIp = clientIp
        self.errorUrl = errorUrl
        self.statusCode = statusCode
        self.errorPayload = errorPayload
        self.errorMessage = errorMessage


