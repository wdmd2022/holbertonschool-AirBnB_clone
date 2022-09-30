#!/usr/bin/python3
""" base_model module for HBNB console project"""
from datetime import datetime, time
from models import storage
import uuid

time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Base Model class for HBNB Console.
    This module contains:
    Public it attribute
    Public created_at attribute
    Public updated_at attribute
    __str__ overwrite to print [<class name>] (<self.id>) <self.__dict__>
    Public method save(self)
    Public method to_dict(self)"""

    def __init__(self, *args, **kwargs):
        """ Instantiate Public Attributes"""

        if kwargs:
            for kee in kwargs:
                if kee == "created_at":
                    self.created_at = datetime.strptime(
                        kwargs["created_at"], time_format)
                if kee == "updated_at":
                    self.updated_at = datetime.strptime(
                        kwargs["updated_at"], time_format)
                if kee != ('__class__'):
                    setattr(self, kee, kwargs[kee])

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Override the string to print [<class name>] (<self.id>) <self.__dict__>"""
        return ("[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__))
