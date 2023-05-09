#!/usr/bin/python3
"""This module defines the class State that inherits from class BaseModel"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os

storage_type = os.getenv("HBNB_TYPE_STORAGE")
class State(BaseModel, Base):
    """Defines the methods and attributes of the class"""

    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade="all, delete, delete-orphan")
    else:
        name = ''

        @property
        def cities(self):
            """
            Returns the list of City instances with state_id equals
            to the current State.id.
            """
            from models import storage

            city_instances = {}
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    city_instances.append(value)
            return city_instances

    def __init__(self, *args, **kwargs):
        """Initializes the attributes of the class"""

        super().__init__(*args, **kwargs)
