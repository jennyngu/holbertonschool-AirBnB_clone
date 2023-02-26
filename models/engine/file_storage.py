#!/usr/bin/python3
"""
A class named FileStorage
The class serialises instances to  JSON file and
deserialises JSON files to instances
"""
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage():

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
        for key, obj in self.__objects.items():
            if isinstance(obj, User):
                obj_dict = obj.to_dict()
                obj_dict['__class__'] = obj.__class__.__name__
            else:
                obj_dict = obj.to_dict()
            objects_dict[key] = obj_dict
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
                if obj_class == "User":
                    obj_instance = User(**value)
                elif obj_class == "Place":
                    obj_instance = Place(**value)
                elif obj_class == "State":
                    obj_instance = State(**value)
                elif obj_class == "City":
                    obj_instance = City(**value)
                elif obj_class == "Amenity":
                    obj_instance = Amenity(**value)
                elif obj_class == "Review":
                    obj_instance = Review(**value)
                else:
                    obj_instance = eval(obj_class)(**value)
                FileStorage.__objects[key] = obj_instance
