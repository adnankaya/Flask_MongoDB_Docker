
# internals
from api import db

class Book(db.Document):
    name = db.StringField(max_length=64)
    author = db.StringField(max_length=32)
    published_year = db.IntField(min=610)

    def __str__(self) -> str:
        return self.name