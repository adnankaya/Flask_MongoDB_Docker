import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # mongo db options
    MONGODB_SETTINGS = [
        {
            "db": os.environ.get("MONGODB_DBNAME","mydb"),
            "host": os.environ.get("MONGODB_HOST","localhost"),
            "port": int(os.environ.get("MONGODB_PORT")) or 27017,
            "alias": "default",
            "username": os.environ.get("MONGODB_USERNAME","developer"),
            "password": os.environ.get("MONGODB_PASSWORD","developer")
        }
    ]

    # security options
    SECRET_KEY = os.environ.get('SECRET_KEY', 'top-secret!')