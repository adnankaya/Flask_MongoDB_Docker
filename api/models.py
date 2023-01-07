
# internals
from api import db


class Author(db.Document):
    firstname = db.StringField(max_length=64)
    lastname = db.StringField(max_length=64)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Book(db.Document):
    name = db.StringField(max_length=64)
    author = db.ReferenceField(document_type=Author)
    published_year = db.IntField(min=610)

    def __str__(self) -> str:
        return self.name
