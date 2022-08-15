from .schema import Book
from .schema import Users
    
def get_books():
    return [
        Book(
            title='The Great Gatsby',
            author='F. Scott Fitzgerald',
        ),
    ]
    
def get_users():
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
