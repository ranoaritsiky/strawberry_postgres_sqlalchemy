from sqlalchemy.orm import Session
from sqlalchemy import select
from app.model import models

from app.session.sessions import engine

from .schema import Book
from .schema import Users
    
def get_books():
    return [
        Book(
            title='The Great Gatsby',
            author='F. Scott Fitzgerald',
        ),
    ]
    
async def get_users():
    query=select(models.User)
    with Session(engine) as session:
        result=session.execute(query)
        for val in result: print(val)
    return[Users(
        first_name='rakoto',
        last_name='frah',
        password='123',
        email='rakoto@gmail.com',
    ),
    Users(
        first_name='peta',
        last_name='korona',
        password='123',
        email='peta@gmail.com',
    ),
    ]
