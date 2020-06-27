#!/usr/bin/python3
import json
from models.base_model import BaseModel
from datetime import datetime


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        new_dictio = {}

        def myconverter(o):
            if isinstance(o, datetime):
                return o.__str__()

        for key in self.__objects:
            new_dictio[key] = self.__objects[key].to_dict()
        with open(self.__file_path, mode="w", encoding="utf8") as file:
            json.dump(new_dictio, file, default=myconverter)

    def reload(self):
        with open(self.__file_path, mode="r") as file:
            open_file = json.loads(file.read())
            for key, value in open_file:
                load_file = BaseModel(**value)
                self.__objects[key] = load_file
