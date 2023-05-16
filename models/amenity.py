#!/usr/bin/python3
"""This module defines the class Amenity that inherits from class BaseModel"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import os


class Amenity(BaseModel, Base):
    """Defines the methods and attributes of the class"""

    __tablename__ = 'amenities'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the attributes of the class"""

        super().__init__(*args, **kwargs)
