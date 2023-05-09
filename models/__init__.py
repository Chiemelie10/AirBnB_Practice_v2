#!/usr/bin/python3
""" Creates a unique FileStorage instance for the application"""

import os

storage_type = os.getenv("HBNB_TYPE_STORAGE",
                         "Please provide storage type")
"""
if storage_type == 'db':
    from models.engine.db_storage import DBStorage

    storage = DBStorage()
    storage.reload()
else:
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
