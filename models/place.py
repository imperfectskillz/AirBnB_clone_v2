#!/usr/bin/python3
'''
    Define the class Place.
'''
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))

class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''
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
    amenity_ids = []
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review",
                               backref="place", cascade="delete")
        amenities = relationship("Amenity",
                                 secondary=place_amenity, viewonly=False)
    else:
        @property
        def reviews(self):
            """gets list of review objs where place_id == Place.id"""
            review_dict = models.storage.all(Review)
            return [review for review in review_dict.values()
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """gets list of Amenity objs where amenity is linked to Place"""
            amenity_dict = {}
            amenity_dict = models.storage.all(Amenity)
            return [amenity for amenity in amenity_dict.values()
                    if amenity.amenity_id == self.id]

        @amenities.setter
        def amenities(self, obj):
            """sets file storage"""
