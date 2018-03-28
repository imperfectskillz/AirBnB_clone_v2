#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    '''
        Definition of the User class
    '''
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    __tablename__ = 'users'
