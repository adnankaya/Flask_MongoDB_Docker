from flask import Blueprint, jsonify, abort
from apifairy import response, body
from apifairy.exceptions import ValidationError
# internals
from .models import Book, Author
from .schemas import AuthorSchema, BookSchema

books_bp = Blueprint("books", __name__)

books_schema = BookSchema(many=True)
book_schema = BookSchema()
author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)
update_author_schema = AuthorSchema(partial=True)


@books_bp.route("/authors/", methods=["POST"])
@body(author_schema)
@response(author_schema, status_code=201)
def create_author(payload):
    author = Author(**payload)
    author.save()
    return author


@books_bp.route("/books/", methods=["POST"])
@body(book_schema)
@response(book_schema, status_code=201)
def create_book(payload):
    author_id = payload.pop("author_id")
    try:
        author = Author.objects.get(id=author_id)
    except Author.DoesNotExist as exc:
        return abort(code=400,
                     description="Author does not exist, check your author_id again")
    else:
        book = Book(**payload, author=author)
        book.save()
        return book


@books_bp.route("/books/", methods=["GET"])
@response(books_schema)
def books():
    book_list = Book.objects.all()

    return book_list


@books_bp.route("/authors/", methods=["GET"])
@response(authors_schema)
def authors():
    author_list = Author.objects.all()

    return author_list


@books_bp.route("/authors/<string:id>", methods=["PUT", "PATCH"])
@body(update_author_schema)
@response(author_schema, status_code=200)
def update_author(payload, id):
    try:
        author = Author.objects.get(id=id)
        author.update(**payload)
        author.save()
        author.reload()
        return author
    except Author.DoesNotExsit as ex:
        return abort(404, description=ex)
    except:
        return abort(400)


@books_bp.route("/authors/<string:id>", methods=["DELETE"])
def delete_author(id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return jsonify(message=f"Deleted {author}!")
    except Author.DoesNotExsit as ex:
        return abort(404, description=ex)
    except:
        return abort(400)
