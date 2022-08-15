"""structure of the data that clients can query"""
from datetime import date

import typing
import strawberry


@strawberry.type
class Book:
    title: str
    author: str

@strawberry.type
class Users:
    first_name:str
    last_name:str
    password:str
    email:str

@strawberry.type
class Query:
    books: typing.List[Book]

