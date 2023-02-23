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
        objects_dict = {}
        for base_model_key in self.__objects:
            objects_dict[base_model_key] = self.__objects[base_model_key].to_dict()
        #print(f"This is the object dict: {objects_dict}")
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(objects_dict, f)

    def reload(self):
        if not os.path.exists(self.__file_path):
            return
        """
        with open(self.__file_path, encoding="utf-8") as json_file:
            dict_of_base_models = json.load(json_file)
            for base_model_key in dict_of_base_models:
                print(base_model_key)
                print(dict_of_base_models[base_model_key])
                print(BaseModel(dict_of_base_models[base_model_key]))
        """
