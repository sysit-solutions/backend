from freenit.base_config import BaseConfig as FreenitBaseConfig


class MailConfig:
    def __init__(self, host, username, password, port=587, ssl=True):
        self.host = host
        self.port = port
        self.ssl = ssl
        self.username = username
        self.password = password


class BaseConfig(FreenitBaseConfig):
    name = "SysIT"
    version = "0.0.1"
    mail = MailConfig("mail.tilda.center", "office@sysit.solutions", "SisAjTi")


class DevConfig(BaseConfig):
    debug = True
    cookie_secure = False
    dburl = "sqlite:///db.sqlite"


class TestConfig(BaseConfig):
    debug = True
    cookie_secure = False
    dburl = "sqlite:///test.sqlite"


class ProdConfig(BaseConfig):
    secret = "MORESECURESECRET"
