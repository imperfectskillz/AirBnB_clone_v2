#!/usr/bin/python3
'''
    Implementation of the State class
'''

import os
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",
                              backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            """gets list of City objs where state_id=State.id"""
            city_dict = models.storage.all(City)
            return [city for city in city_dict.values()
                    if city.state_id == self.id]
    #name = ""
