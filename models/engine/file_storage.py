#!/usr/bin/python3
"""
A class named FileStorage
The class serialises instances to  JSON file and
deserialises JSON files to instances
"""
import json
import os.path


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dict of __objects
        """
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            for base_model in self.__objects.values():
                json.dump(base_model.to_dict(), f)

    def reload(self):
        if not os.path.exists(self.__file_path):
            return
        with open(self.__file_path, encoding="utf-8") as obj_from_json:
            return(json.load(obj_from_json))
