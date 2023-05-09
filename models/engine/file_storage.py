#!/usr/bin/python3
"""This module defines class FileStorage."""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
        }


class FileStorage():
    """
    This class serializes instances to a JSON file and
    deserializes JSON file to instances.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns the dictionary __objects if cls is None, else it
        returns only the dictionary __objects of the given cls
        """

        if cls is not None:
            dict_of_cls = {}
            dict_of_cls = {k: v for k, v in self.__objects.items()
                           if isinstance(v, cls)}
            return dict_of_cls

        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <class name>.id"""

        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path)"""

        json_dict = {}

        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(json_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists ; otherwise does nothing if the
        file doesn't exist.
        """

        try:
            with open(self.__file_path, 'r') as f:
                pd = json.load(f)
            for key in pd:
                self.__objects[key] = classes[pd[key]["__class__"]](**pd[key])
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it is inside. It does nothing if
        obj is equal to None.
        """
        """
        if obj is not None:
            obj_not_to_del = {}
            for k, v in self.__objects.items():
                if v != obj:
                    obj_not_to_del[k] = v
            self.__objects = obj_not_to_del
        """

        if obj is not None:
            key_to_del = obj.to_dict()['__class__'] + "." + obj.id
            if key_to_del in self.__objects.keys():
                del self.__objects[key_to_del]
