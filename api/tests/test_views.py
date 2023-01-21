from flask import url_for
from api.models import Author, Book
from api.tests.base import BaseTestCase

class ApiViewsTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.author = Author(firstname='John', lastname='Doe').save()
        self.book = Book(name='Test Book', author=self.author, published_year=2000).save()


    def test_create_author(self):
        data = {"firstname": "Jane", "lastname": "Doe"}
        response = self.client.post(url_for("books.create_author"), json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()["firstname"], data["firstname"])
        self.assertEqual(response.get_json()["lastname"], data["lastname"])

    def test_create_book(self):
        data = {"name": "Test Book 2", "author_id": str(self.author.id), "published_year": 2000}
        response = self.client.post(url_for("books.create_book"), json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()["author"]["id"], data["author_id"])
        self.assertEqual(response.get_json()["name"], data["name"])
        self.assertEqual(response.get_json()["published_year"], data["published_year"])

    def test_create_book_invalid_author(self):
        data = {"name": "Test Book 2", "author_id": "invalid_id", "published_year": 2000}
        response = self.client.post(url_for("books.create_book"), json=data)
        self.assertEqual(response.status_code, 400)

    def test_books(self):
        response = self.client.get(url_for("books.books"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)
        self.assertEqual(response.get_json()[0]["name"], self.book.name)
        self.assertEqual(response.get_json()[0]["published_year"], self.book.published_year)
        self.assertEqual(response.get_json()[0]["author"]["firstname"], self.book.author.firstname)
        self.assertEqual(response.get_json()[0]["author"]["lastname"], self.book.author.lastname)

    def test_authors(self):
        response = self.client.get(url_for("books.authors"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)
        self.assertEqual(response.get_json()[0]["firstname"], self.author.firstname)
        self.assertEqual(response.get_json()[0]["lastname"], self.author.lastname)

    def test_update_author(self):
        data = {"firstname": "Jane"}
        response = self.client.put(url_for("books.update_author", id=self.author.id), json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["firstname"], data["firstname"])

    def test_update_author_invalid_id(self):
        data = {"firstname": "Jane"}
        # 'invalid_id' is not a valid ObjectId, it must be a 12-byte input or a 24-character hex string
        response = self.client.put(url_for("books.update_author", id="invalid_id"), json=data)
        self.assertEqual(response.status_code, 400)

    def test_delete_author(self):
        response = self.client.delete(url_for("books.delete_author", id=self.author.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "Deleted John Doe!"})

    def test_delete_author_invalid_id(self):
        # 'invalid_id' is not a valid ObjectId, it must be a 12-byte input or a 24-character hex string
        response = self.client.delete('/api/v1/authors/invalid_id')
        self.assertEqual(response.status_code, 400)

    