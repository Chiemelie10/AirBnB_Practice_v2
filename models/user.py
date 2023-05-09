#!/usr/bin/python3
"""This module defines class User that inherits from class BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """Defines the users of the application."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """defines the instance attributes of class User."""

        super().__init__(*args, **kwargs)
