#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from datetime import datetime
import os


class FileStorage:

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
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes to the JSON file
        """
        new_dictio = {}

        def myconverter(obj):
            """convert obj to str

            Args:
                obj (obj): object to convert

            Returns:
                obj: obj str representarion
            """
            if isinstance(obj, datetime):
                return obj.__str__()

        for key in self.__objects:
            new_dictio[key] = self.__objects[key].to_dict()
        with open(self.__file_path, mode="w", encoding="utf8") as file:
            json.dump(new_dictio, file, default=myconverter)

    def reload(self):
        """ deserializes the JSON file

        Returns:
            obj: objec dict
        """
        if not os.path.isfile(self.__file_path):
            return self.__objects
        else:
            with open(self.__file_path, mode="r") as file:
                file_data = json.load(file)
            for key, value in file_data.items():
                self.__objects[key] = eval(value["__class__"])(**value)
