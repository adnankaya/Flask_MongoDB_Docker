from flask import Blueprint, jsonify
# internals
from .models import Book

books_bp = Blueprint("books", __name__)


@books_bp.route("/books/", methods=["GET"])
def books():
    book_list = Book.objects.all()
    
    return jsonify(book_list)