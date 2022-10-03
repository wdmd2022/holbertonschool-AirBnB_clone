#!/usr/bin/python3
"""This module holds the command interpreter"""

import cmd
import readline
from models.engine.file_storage import FileStorage
from models import storage

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class_example = {"BaseModel": BaseModel,
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

    def do_quit(self, args):
        """
        quit command exits the program
        """
        raise SystemExit

    def do_EOF(self, args):
        """
        Exits the application on End of File
        """
        raise SystemExit

    def emptyline(self):
        """
        If the line is empty, don't do a darn thing
        (please pardon my french)
        """
        pass

    def do_show(self, args):
        """ Prints the string representation of an
        instance based on the class name and ID.
        If the class name is missing it will print:
        ** class name missing **

        If the ID does not exist, it will print:
        ** class id missing **

         If the instance of the class name doesn't exist for the id, prints:
            ** no instance found **
        """

        arg_list = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif arg_list[0] in class_example.keys():
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                obj_search = arg_list[0] + "." + arg_list[1]
                obj_all = storage.all()
                if obj_search in obj_all:
                    print(str(obj_all[obj_search]))
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id
        and saves the change into the JSON file
        If the class name is missing, print:
        ** class name missing **

        If the class name does not exist, print:
        ** class doesn't exist **

        If the id is missing, print:
        ** instance id missing **

        If the instance of the class name does not exist for the id, print:
        ** no instance found **
        """
        pass

    def do_all(self, args):
        """Prints all string representation of all object instances
        based on the class name given.
        If no class name is given, prints all object instances.
        The printed result will be a list of strings
        If the class name doesn't exist, prints:
            ** class doesn't exist **
        """
        pass

    def do_update(self, args):
        """Updates an instance based on the class name and ID or
        by adding or updating attributes (saved to the JSON file)"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
