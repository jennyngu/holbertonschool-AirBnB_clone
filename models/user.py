#!/usr/bin/python3
"""
A class named User
"""
from models import storage
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
