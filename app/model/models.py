from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship

from ..session.sessions import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, unique=True, index=True)
    last_name = Column(String)
    email = Column(String, default=True)
    password = Column(String, default=True)



