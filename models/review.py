#!/usr/bin/python3
"""This module defines the class Review that inherits from class BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Defines the methods and attributes of the class"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes the attributes of the class"""

        super().__init__(*args, **kwargs)
