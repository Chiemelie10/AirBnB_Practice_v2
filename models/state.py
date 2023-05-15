#!/usr/bin/python3
"""This module defines the class State that inherits from class BaseModel"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel, Base):
    """Defines the methods and attributes of the class"""

    __tablename__ = 'states'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete, delete-orphan',
                              backref='state')
    else:
        name = ""

        @property
        def cities(self):
            """
            Returns list of City instances with state_id equals
            to the current state,id.
            """
            from models import storage

            cities_in_state = []
            city_dict = storage.all(City)

            for value in city_dict.values():
                if state_id == self.id:
                    cities_in_state.append(value)
            return cities_in_state

    def __init__(self, *args, **kwargs):
        """Initializes the attributes of the class"""

        super().__init__(*args, **kwargs)
