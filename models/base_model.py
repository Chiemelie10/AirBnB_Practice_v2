#!/usr/bin/python3
""" This module defines class BaseModel"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes the public instance attributes of class BaseModel"""

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if hasattr(self, 'created_at') and type(self.created_at) is str:
                self.created_at = datetime.strptime(self.created_at,
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in dir(self) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(self.updated_at,
                                                    '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """Prints a string representation of the object"""

        class_name = self.__class__.__name__
        _id = self.id
        attributes_dict = self.__dict__

        return "[{}] ({}) {}".format(class_name, _id, attributes_dict)

    def save(self):
        """
        Updates the public instance attribute updated_at with the
        current date time.
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """

        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = datetime.isoformat(self.created_at)
        instance_dict['updated_at'] = datetime.isoformat(self.updated_at)

        return instance_dict
