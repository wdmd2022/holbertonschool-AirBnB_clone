#!/usr/bin/python3
"""Module with unit tests for the BaseModel Class"""
from models.engine.file_storage import file_storage
import unittest


class Test_FileStorage_Documentation(unittest.TestCase):
    """Contains tests for the doc strings in FileStorage"""

    def test_module_docs(self):
        """Checks for documentation in file_storage module"""
        self.assertGreaterEqual(len(file_storage.__doc__), 1)

    def test_class_docs(self):
        """Checks for documentation of FileStorage"""
        self.assertGreaterEqual(len(file_storage.FileStorage.__doc__), 1)

if __name__ == '__main__':
    unittest.main()
