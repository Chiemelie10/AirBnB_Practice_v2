#!/usr/bin/python3
"""This module defines the class City that inherits from class BaseModel"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class City(BaseModel, Base):
    """Defines the methods and attributes of the class"""

    __tablename__ = 'cities'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', cascade='all, delete, delete-orphan',
                              backref='cities')
    else:
        state_id = name = ''

    def __init__(self, *args, **kwargs):
        """Initializes the attributes of the class"""

        super().__init__(*args, **kwargs)
