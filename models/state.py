#!/usr/bin/python3
'''
    Implementation of the State class
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete-orphan",
                              backref="state")

    else:
        name = ""

        @property
        def cities(self):
            city_list = []
            city_dict = models.storage.all(City)
            for k, v in city_dict.items():
                if v.state_id == self.id:
                    city_list.append(value)
            return city_list
