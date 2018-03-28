#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    '''
        Definition of the User class
    '''
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    __tablename__ = 'users'
    places = relationship("Place",
                          backref=("user", cascade="delete"))
    reviews = relationship("Review",
                           backref=("user", cascade="delete"))
