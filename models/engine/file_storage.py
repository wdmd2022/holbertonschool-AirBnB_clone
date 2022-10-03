#!/usr/bin/python3
"""this module contains the class File Storage"""

import json
import os.path
from types import ClassMethodDescriptorType
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """class that serializes instances to a JSON file, and
    deserializes a JSON file to instances"""
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary storing all objects by <class name>.id
        i.e., a BaseModel object with id=8675309 would be stored with the
        key BaseModel.8675309"""
        return self.__objects
    
    
    def new(self, obj):
        """sets in the dictionary __objects, the obj and gives it the key
        in the format of <obj class name>.id"""
        if obj:
            self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """serializes the dictionary __objects to the JSON file with the
        path of __file_path, which allows us to store the objects"""
        dicty = {}
        pydict = FileStorage.__objects
        for key in pydict.keys():
            dicty.update({key : pydict[key].to_dict()})


    # def save(self):
    #     """serializes the dictionary __objects to the JSON file with the
    #     path of __file_path, which allows us to store the objects"""
    #     dicttodump = {}
    #     for quay in self.__objects:
    #         dicttodump[quay] = self.__objects[quay].to_dict()
    #     with open(self.__file_path, 'w') as a_file:
    #         json.dump(dicttodump, a_file)

    def classreturn(self):
        """returns the classes associated with the strings of their names"""
        class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }
        return class_dict
    
    
    def reload(self):
        """deserializes the JSON file with the path of '__file_path' to
        __objects, if it exists; otherwise, this method does nothing and
        doesn't even raise an exception because we're extremely reasonable
        people who write extremely reasonable code"""
        # if os.path.exists(self.__file_path):
        classreturn = classreturn(self)
        try:
            with open(self.__file_path, 'r') as file_that_exists:
                deserialized_dict = json.load(file_that_exists)
                for key, value in deserialized_dict.items():
                    classtype = value["__class__"]
                    self.__objects[key] = classreturn[classtype](**value)
        except Exception:
            pass
                # THIS IS WHERE I LEFT OFF
                # THIS FUNCTION IS NOT DONE
