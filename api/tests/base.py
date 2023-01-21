import unittest
#  internals
from api import db, create_app
from config import Config


class TestConfig(Config):
    SERVER_NAME = '127.0.0.1:5000'
    TESTING = True
    MONGODB_SETTINGS = [
        {
            "db": "test_db",
            "host": "mymongodb", # our docker db host name
            "port": 27017,
            "alias": "default",
            "username": "developer",
            "password": "developer",
            "connect": False,
        }
    ]


class BaseTestCase(unittest.TestCase):
    '''
    Run: docker compose exec web sh -d  "pytest -s --disable-warnings"
    '''
    config = TestConfig

    def setUp(self):
        db.disconnect("default")
        #  create flask app
        self.app = create_app(self.config)
        self.app_context = self.app.app_context()
        self.app_context.push()
        #  drop previous existing data
        db.connection["default"].drop_database("test_db")
        self.client = self.app.test_client()

    def tearDown(self):
        db.connection["default"].drop_database("test_db")
        db.disconnect()
        self.app_context.pop()
