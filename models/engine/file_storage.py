#!/usr/bin/python3
"""
A class named FileStorage
The class serialises instances to  JSON file and
deserialises JSON files to instances
"""
import json
import os.path
from models.base_model import BaseModel


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dict of __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        objects_dict = {}
        for base_model_key in self.__objects:
            objects_dict[base_model_key] = \
                self.__objects[base_model_key].to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(objects_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects if it exists
        """
        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, encoding="utf-8") as json_file:
            dict_obj = json.load(json_file)
            for key, value in dict_obj.items():
                obj_class = value["__class__"]
                obj_instance = eval(obj_class)(**value)
                FileStorage.__objects[key] = obj_instance
