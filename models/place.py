#!/usr/bin/python3
'''
    Define the class Place.
'''
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review",
                               backref="place", cascade="delete")
    else:
        @property
        def reviews(self):
            """gets list of review objs where place_id == Place.id"""
            review_dict = models.storage.all(Review)
            return [review for review in review_dict.values()
                    if review.place_id == self.id]
    #city_id = ""
    #user_id = ""
    #name = ""
    #description = ""
    #number_rooms = 0
    #number_bathrooms = 0
    #max_guest = 0
    #price_by_night = 0
    #latitude = 0.0
    #longitude = 0.0
    #amenity_ids = []
