#!/usr/bin/python3
"""This module defines the class Review that inherits from class BaseModel"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import os


class Review(BaseModel, Base):
    """Defines the methods and attributes of the class"""

    __tablename__ = 'reviews'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """Initializes the attributes of the class"""

        super().__init__(*args, **kwargs)
