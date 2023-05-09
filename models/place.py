#!/usr/bin/python3
"""This module defines the class Place that inherits from class BaseModel"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Defines the methods and attributes of the class"""

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

    def __init__(self, *args, **kwargs):
        """Initializes the attributes of the class"""

        super().__init__(*args, **kwargs)
