#!/usr/bin/python3
'''
    Define the class City.
'''
from models.base_model import BaseModel, Base 
from sqlalchemy import Table, Column, ForeignKey, String


class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    state_id = Column(String(60), nullable=False, ForeignKey('states.id'))
    name = Column(String(128), nullable=False)
    __tablename__ = 'cities'
