import typing
import strawberry
from .schema import Book
from .schema import Users
from .handler import get_books
from .handler import get_users

@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)
    users:typing.List[Users]=strawberry.field(resolver=get_users)