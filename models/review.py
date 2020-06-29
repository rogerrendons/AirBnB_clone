#!/usr/bin/python3
"""models module
    """
from models.base_model import BaseModel

class Review(BaseModel):
    """[summary]

    Args:
        BaseModel ([type]): [description]
    """
    place_id = ""
    user_id = ""
    text = ""
