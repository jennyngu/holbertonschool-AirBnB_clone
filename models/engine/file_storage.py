#!/usr/bin/python3
"""
Import BaseModel
"""
from models.base_model import BaseModel
import json


class FileStorage:
    """
    FlieStorage
    """
    def __init__(self, file_path=None, objects=None):
        """
        Initialization
        """
        path = FileStorage.__name__        
        self.__file_path = f"./{path}.json"
        self.__objects = {}

    def all(slef):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects[f"{obj}"] = obj.id

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        filename = self.__name__ + ".json"
        with open(filename, 'w') as f:
            return json.dump(self.__object, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path)
        exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
        path = f"./{self.__name__}.json"
        if not os.path.exists(path):
            return
        with open (f"./{self.__name__}.json", 'r') as f:
            x = json.reload(f.read())
        return x
