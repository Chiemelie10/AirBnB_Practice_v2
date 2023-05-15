#!/usr/bin/python3
"""This module defines the class Place that inherits from class BaseModel"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import os


class Place(BaseModel, Base):
    """Defines the methods and attributes of the class"""

    __tablename__ = 'places'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """
            Returns the list of Review instances with place_id equals
            to the current place.id.
            """
            from models import storage
            from models.review import Review

            review_of_place = []
            review_dict = storage.all(Review)
            for obj in review_dict.values():
                if obj.place_id == self.id:
                    review_of_place.append(obj)
            return review_of_place


    def __init__(self, *args, **kwargs):
        """Initializes the attributes of the class"""

        super().__init__(*args, **kwargs)
