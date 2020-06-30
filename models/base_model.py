#!/usr/bin/python3
"""models module
    """
from datetime import datetime
import models
import uuid


class BaseModel:
    """[summary]
    """

    def __init__(self, *args, **kwargs):
        """[summary]
        """
        if kwargs:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    at_to_set = datetime.strptime(value, time_format)
                    setattr(self, key, at_to_set)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Str representation of BaseModel
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """create dict representation of an object

        Returns:
            dict: object dict representation
        """
        dict_representation = self.__dict__.copy()
        dict_representation["__class__"] = self.__class__.__name__
        dict_representation["created_at"] = self.created_at.isoformat()
        dict_representation["updated_at"] = self.updated_at.isoformat()

        return dict_representation
