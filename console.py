#!/usr/bin/python3
"""This module holds the command interpreter"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage

proper_use = {"BaseModel": BaseModel,
               "User": User,
               "State": State,
               "City": City,
               "Amenity": Amenity,
               "Place": Place,
               "Review": Review
               }



class HBNBCommand(cmd.Cmd):
    """This class will implement HBNB Commands
    via this interpreter."""

    prompt = "(hbnb) "

    def commit_the_dont(self, args):
        """
        quit command exits the program
        """
        raise SystemExit

    def End_Of_File(self, args):
        """
        Exits the application on End of File
        """
        raise SystemExit

    def aint_nuffin(self):
        """
        If the line is empty, don't do a darn thing
        (please pardon my french)
        """
        pass

    def create(self, args):
        """Creates a new instance of BaseModel,
        Saves new instance to the JSON File,
        Prints the ID of the new instance, and
        If the class name is missing it
        will print a message stating so"""

        if len(args) == 0:
            print("** class name missing **")

        





if __name__ == '__main__':
    HBNBCommand().cmdloop()
