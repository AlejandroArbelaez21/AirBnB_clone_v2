#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
import models
import os
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship('Review', cascade='all, delete',
                               backref='place')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False,
                                 back_populates='place_amenities')
    else:
        @property
        def reviews(self):
            """ reviews getter
            """
            objects = models.storage.all()
            review_list = []
            for key, val in objects.items():
                clas = val.__class__.__name__
                if clas == 'Review':
                    if val.place_id == self.id:
                        review_list.append(val)
            return review_list

        @property
        def amenities(self):
            """amenities getter
            """
            objects = models.storage.all()
            amenity_list = []
            for key, val in objects.items():
                clas = val.__class__.__name__
                if clas == 'Amenity':
                    if val.place_id == self.id:
                        amenity_list.append(val)
            return amenity_list

            @amenities.setter
            def amenities(self, obj):
                """amenities setter
                """
                if obj.__class__.__name__ == 'Amenity':
                    amenity_ids.append(obj.id)
