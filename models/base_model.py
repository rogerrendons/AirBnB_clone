#!/usr/bin/python3
"""models module
    """
from datetime import datetime
import models
import uuid

time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """[summary]
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == "created_at":
                    self.created_at = datetime.strptime(
                        kwargs["created_at"], time_format)
                if key == "update_at":
                    self.updated_at = datetime.strptime(
                        kwargs["update_at"], time_format)
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

        if "created_at" in dict_representation:
            dict_representation["created_at"] = self.created_at.isoformat()

        if "update_at" in dict_representation:
            dict_representation["updated_at"] = self.updated_at.isoformat()

        return dict_representation
