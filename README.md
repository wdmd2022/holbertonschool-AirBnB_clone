# AirBnB Clone: The Console
project for Holberton School Tulsa, Fall 2022

#### The First Step: A command interpreter to manage future versions
As the first step toward building a fully-fledged web applicaiton, this project lays the foundation
for data structures crucial to making a clone of the (original) AirBnB web application.

##### The tasks represented here will allow us to:
* create a parent class (BaseModel) to carry out the initialization, serialization, and deserialization of future instances
* move data through a simple flow of serialization/deserialization, from Instance, to Dictionary, to JSON string, file and back again
* create crucial classes used in the AirBnB clone project that will inherit from BaseModel (such as User, State, City, Place...)
* create our initial asbstracted storage engine of the AirBnB clone project (File storage)
* demonstrate and test the functionality of our project through unittesting

#### our command interpreter will allow us to:
* create a new object
* retrieve said objects from a file (subsequently, a database)
* operate upon our objects (count, compute stats, etc...)
* update object attributes
* remove/delete objects from storage

#### learning objectives as stated in the course:
##### Students should, at the end of the project, be able to explain to anyone:
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

#### Project Technical Requirements
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

#### Unit Test Requirements
* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the unittest module
* All your test files should be python files (extension: .py)
* All your test files and folders should start by test_
* Your file organization in the tests folder should be the same as your project
e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
* All your tests should be executed by using this command: python3 -m unittest discover tests
* You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
