#!/usr/bin/python3
"""This module defines the class Amenity that inherits from class BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines the methods and attributes of the class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the attributes of the class"""

        super().__init__(*args, **kwargs)
