#!/usr/bin/python3
"""This module defines class User that inherits from class BaseModel"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class User(BaseModel, Base):
    """Defines the users of the application."""

    __tablename__ = 'users'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship('Place',
                              cascade='all, delete, delete-orphan',
                              backref='user')
        reviews = relationship('Review', backref='user',
                               cascade='all, delete, delete-orphan')
    else:
        email = password = first_name = last_name = ''

    def __init__(self, *args, **kwargs):
        """defines the instance attributes of class User."""

        super().__init__(*args, **kwargs)
