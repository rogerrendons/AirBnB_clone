#!/usr/bin/python3
"""models module
    """
from models.base_model import BaseModel


class User(BaseModel):
    """[summary]

    Args:
        BaseModel ([type]): [description]
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
