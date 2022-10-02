#!/usr/bin/python3
"""this module contains the class File Storage"""

import json
import os.path
from models.base_model import BaseModel

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
        dicttodump = {}
        for quay in self.__objects:
            dicttodump[quay] = self.__objects[quay].to_dict()
        with open(self.__file_path, 'w') as a_file:
            json.dump(dicttodump, a_file)


    def reload(self):
        """deserializes the JSON file with the path of '__file_path' to
        __objects, if it exists; otherwise, this method does nothing and
        doesn't even raise an exception because we're extremely reasonable
        people who write extremely reasonable code"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file_that_exists:
                deserialized_dict = json.load(file_that_exists)
                for key in deserialized_dict:
                    self.__objects[key] = getattr(deserialized_dict[key])
                # THIS IS WHERE I LEFT OFF
                # THIS FUNCTION IS NOT DONE
