#!/usr/bin/python3
"""
Base Class
"""
import uuid
import datetime
import models


class BaseModel:
    """
    BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """
        Initialisation
        """
        if kwargs != {}:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'created_at':
                    self.created_at = datetime.datetime.fromisoformat(value)
                elif key == 'updated_at':
                    self.updated_at = datetime.datetime.fromisoformat(value)
                elif key == 'my_number':
                    self.my_number = value
                elif key == 'name':
                    self.name = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Print str format: [<class name>] (<self.id>) <self.__dict__>
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        Updates the attribute updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["updated_at"] = self.updated_at.isoformat()
        inst_dict["id"] = self.id
        inst_dict["created_at"] = self.created_at.isoformat()

        return inst_dict
