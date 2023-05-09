#!/usr/bin/python3
"""This module defines the class DBStroge"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    """Defines the methods of the data base storage."""

    __engine = None
    __session = None
    __classes = {
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def __init__(self):
        """Defines the instance attributes."""

        dev_environ = os.getenv("HBNB_ENV", "Please set environment")
        user = os.getenv("HBNB_MYSQL_USER", "Please set user")
        password = os.getenv("HBNB_MYSQL_PWD", "Please set password")
        host = os.getenv("HBNB_MYSQL_HOST", "Please set host")
        database = os.getenv("HBNB_MYSQL_DB", "Please set database")
        port = 3306

        url = "mysql+mysqldb://{}:{}@{}:{}/{}".format(user, password,
                                                      host, port, database)

        self.__engine = create_engine(url, pool_pre_ping=True)

        if dev_environ == "test":
            Base.metadata.drop_all(self.__engine)
    """

    def all(self, cls=None):
        
        Returns the instances of all classes if cls is None. Otherwise,
        it returns all instances of the provided class
        
        objs_dict = {}

        if cls is not None:
            objs_of_given_cls = self.__session.query(cls)
            for obj in objs_of_given_cls.all():
                obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objs_dict[obj_key] = obj
        else:
            for _cls in self.__classes.values():
                objs_of_class = self.__session.query(_cls)
                for obj in objs_of_class.all():
                    obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objs_dict[obj_key] = obj

        return objs_dict
    """

    def new(self, obj):
        """Adds an object to the current database session"""

        if isinstance(obj, BaseModel):
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as e:
                self.__session.rollback()
                raise e

    def save(self):
        """Commits all changes to the current database session"""

        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session obj if not None"""

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads all the tables from the database."""

        Base.metadata.create_all(self.__engine, checkfirst=True)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session
