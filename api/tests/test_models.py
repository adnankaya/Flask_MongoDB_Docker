from api.models import Author, Book
from api.tests.base import BaseTestCase


class TestAuthorModel(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.author = Author(firstname='John', lastname='Doe')

    def test_author_str_representation(self):
        self.assertEqual(str(self.author), 'John Doe')

    def test_author_save(self):
        self.author.save()
        result = Author.objects(firstname='John', lastname='Doe')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].firstname, 'John')
        self.assertEqual(result[0].lastname, 'Doe')


class TestBookModel(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.author = Author(firstname='John', lastname='Doe').save()
        self.book = Book(name='Test Book', author=self.author,
                         published_year=2000)

    def test_book_str_representation(self):
        self.assertEqual(str(self.book), 'Test Book')

    def test_book_save(self):
        self.book.save()
        result = Book.objects(name='Test Book')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, 'Test Book')
        self.assertEqual(str(result[0].author), 'John Doe')
        self.assertEqual(result[0].published_year, 2000)
