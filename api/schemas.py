from marshmallow import validate
#  internals
from api import marsh as ma


class AuthorSchema(ma.Schema):

    lastname = ma.String(required=True)
    firstname = ma.String(required=True)
    id = ma.String(unique=True, dump_only=True)

    class Meta:
        ordered = True


class BookSchema(ma.Schema):

    id = ma.String(unique=True, dump_only=True)
    name = ma.String(required=True)
    author = ma.Nested(AuthorSchema, dump_only=True)
    author_id = ma.String(load_only=True, required=True)
    published_year = ma.Integer(strict=True, required=True,
                                validate=[validate.Range(
                                    min=610, error="Year must be min 610")]
                                )

    class Meta:
        ordered = True
