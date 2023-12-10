#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the storage dictionary.

        Args:
            obj (BaseModel): The object to be added.
        """
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        objects_dict = {key: obj.to_dict() for key,
                        obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as file:
                objects_dict = json.load(file)
                for obj_data in objects_dict.values():
                    cls_name = obj_data["__class__"]
                    del obj_data["__class__"]
                    self.new(eval(cls_name)(**obj_data))
        except FileNotFoundError:
            pass
