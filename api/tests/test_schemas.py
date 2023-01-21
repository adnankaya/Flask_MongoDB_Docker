from marshmallow import ValidationError
from api.models import Author, Book
from api.schemas import AuthorSchema, BookSchema
from api.tests.base import BaseTestCase

class TestAuthorSchema(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.author = Author(firstname='John', lastname='Doe')
        self.schema = AuthorSchema()

    def test_author_schema_dump(self):
        result = self.schema.dump(self.author)
        result.pop("id")
        self.assertEqual(result, {"lastname": "Doe", "firstname": "John"})

    def test_author_schema_load(self):
        data = {"lastname": "Doe", "firstname": "John"}
        result = self.schema.load(data)
        self.assertEqual(result, {"lastname": "Doe", "firstname": "John"})

    def test_author_schema_load_missing_field(self):
        data = {"lastname": "Doe"}
        with self.assertRaises(ValidationError):
            self.schema.load(data)


class TestBookSchema(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.author = Author(firstname='John', lastname='Doe').save()
        self.book = Book(name='Test Book', author=self.author, published_year=2000)
        self.schema = BookSchema()

    def test_book_schema_dump(self):
        result = self.schema.dump(self.book)
        result.pop("id")
        author = result.pop("author")
        author.pop("id")
        self.assertEqual(result, {"name": "Test Book", "published_year":2000})
        self.assertEqual(author, {"lastname": "Doe", "firstname": "John"})

    def test_book_schema_load(self):
        data = {"name": "Test Book", "author_id": str(self.author.id), "published_year": 2000}
        result = self.schema.load(data)
        self.assertEqual(result, {"name": "Test Book", "author_id": str(self.author.id), "published_year": 2000})

    def test_book_schema_load_missing_field(self):
        data = {"name": "Test Book", "published_year": 2000}
        with self.assertRaises(ValidationError):
            self.schema.load(data)

    def test_book_schema_load_invalid_year(self):
        data = {"name": "Test Book", "author_id": str(self.author.id), "published_year": 600}
        with self.assertRaises(ValidationError):
            self.schema.load(data)


