#!/usr/bin/python3
"""This module defines the class Place that inherits from class BaseModel"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Table
import os


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity',
                          Base.metadata,
                          Column('place_id',
                                 String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id',
                                 String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False))

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
        amenities = relationship('Amenity', backref='place_amenities',
                                 secondary=place_amenity, viewonly=False)
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

        @property
        def amenities(self):
            """
            Returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the place
            """

            from models import storage
            from models.amenity import Amenity

            amenities_of_place = []
            amenity_dict = storage.all(Amenity)

            for obj in amenity_dict.values():
                if obj.id in self.amenity_ids:
                    amenities_of_place.append(obj)
            return amenities_of_place

        @amenities.setter
        def amenities(self, obj):
            """Append amenity 'id' to the list of amenity ids"""

            if type(obj) != Amenity:
                return

            if obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)


    def __init__(self, *args, **kwargs):
        """Initializes the attributes of the class"""

        super().__init__(*args, **kwargs)
