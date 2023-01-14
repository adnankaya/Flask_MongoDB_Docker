from flask import Flask
from flask_mongoengine import MongoEngine
from flask_marshmallow import Marshmallow
# from apifairy import APIFairy

# internals
from config import Config


db = MongoEngine()
marsh = Marshmallow()
# apifairy = APIFairy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # database mongodb
    db.init_app(app)

    # # serialization/deserialization Marshmallow
    marsh.init_app(app)

    # # api documentation
    # apifairy.init_app(app)
    
    # blueprints
    API_URL_PREFIX = "/api/v1"
    from api.views import books_bp

    app.register_blueprint(books_bp, url_prefix=API_URL_PREFIX)
    

    return app
