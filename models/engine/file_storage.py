#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from datetime import datetime


class FileStorage:
    """[summary]

    Returns:
        [type]: [description]
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns:
            dict: dictionary objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id

        Args:
            obj (obj): obj to set format
        """
        FileStorage.__objects["{}.{}"
                              .format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes to the JSON file
        """
        new_dictio = {}

        with open(self.__file_path, mode="w", encoding="utf8") as file:
            for key, value in self.__objects.items():
                new_dictio[key] = value.to_dict()
            json.dump(new_dictio, file)

    def reload(self):
        """ deserializes the JSON file

        Returns:
            obj: objec dict
        """
        if not os.path.isfile(self.__file_path):
            return self.__objects
        else:
            with open(self.__file_path, mode="r", encoding="utf8") as file:
                file_data = json.load(file)
            for key, value in file_data.items():
                self.__objects[key] = eval(value["__class__"])(**value)
