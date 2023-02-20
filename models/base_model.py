#!/usr/bin/python3
"""
Base Class
"""


import uuid
import datetime

class BaseModel():
    """
    BaseModel class
    """
    def __init__(self):
        """
        Initialisation
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Print [<class name>] (<self.id>) <self.__dict__>
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        update the attribute updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        """
        self.updated_at = datetime.datetime.now()
        inst_dict = self.__dict__
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["updated_at"] = datetime.datetime.isoformat(self.updated_at)
        inst_dict["id"] = self.id
        inst_dict["created_at"] = datetime.datetime.isoformat(self.created_at)

        return inst_dict
