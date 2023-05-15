#!/usr/bin/python3
"""This module defines the class DBStorage"""

from models.base_model import BaseModel, Base
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.city import City


class DBStorage():
    """Defines the methods of the clsss."""

    __engine = None
    __session = None

    def __init__(self):
        """Defines the instance attributes of the class."""

        passwd = os.getenv('HBNB_MYSQL_PWD', 'Please enter password')
        user = os.getenv('HBNB_MYSQL_USER', 'Please enter user')
        host = os.getenv('HBNB_MYSQL_HOST', 'Please enter host')
        database = os.getenv('HBNB_MYSQL_DB', 'Please enter database')
        port = 3306

        url = "mysql+mysqldb://{}:{}@{}:{}/{}".format(user, passwd,
                                                      host, port, database)
        self.__engine = create_engine(url, pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session (self.__session) all
        objects depending of the class name (argument cls)
        """
        classes = {
            'User': User,
            'State': State,
            'City': City,
            #'Amenity': Amenity,
            'Place': Place,
            #'Review': Review
        }

        objs_dict = {}

        if cls is not None and cls in classes.values():
            objs = self.__session.query(cls)
            for obj in objs.all():
                key = obj.__class__.__name__ + '.' + obj.id
                objs_dict[key] = obj
        elif cls is None:
            for cls_type in classes.values():
                objs = self.__session.query(cls_type)
                for obj in objs.all():
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objs_dict[key] = obj
        return objs_dict

    def new(self, obj):
        """Add the object to the current database session (self.__session)"""

        if isinstance(obj, BaseModel):
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as e:
                self.__session.rollback()
                raise e

    def save(self):
        """Commit all changes of the current database session."""

        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None."""

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database, create the current database
        session from the engine by using sessionmaker.
        """

        Base.metadata.create_all(self.__engine, checkfirst=True)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session
