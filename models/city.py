#!/usr/bin/python3
"""This module defines the class City that inherits from class BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Defines the methods and attributes of the class"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the attributes of the class"""

        super().__init__(*args, **kwargs)
