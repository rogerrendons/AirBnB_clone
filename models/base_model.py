#!/usr/bin/python3
"""models module
    """
from datetime import datetime
import models
import uuid


class BaseModel:
    """[summary]
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Str representation of BaseModel
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """create dict representation of an object

        Returns:
            dict: object dict representation
        """
        to_dict_representation = self.__dict__.copy()

        to_dict_representation["__class__"] = self.__class__.__name__

        if "created_at" in to_dict_representation:
            to_dict_representation["created_at"] = to_dict_representation["created_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")

        if "update_at" in to_dict_representation:
            to_dict_representation["update_at"] = to_dict_representation["update_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
       
        return to_dict_representation
