#!/usr/bin/python3
'''
    Define the class City.
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship
from os import environ


class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

    if environ.get("HBNB_TYPE_STORAGE") == "db":
        places = relationship("Place", cascade="all, delete-orphan",
                              backref="cities")
    else:
        state_id = ""
        name = ""
