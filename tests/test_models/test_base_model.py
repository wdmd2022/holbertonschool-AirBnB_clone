#!/usr/bin/python3
"""Module hlds the unit tests for the BaseModel Class"""
from models import base_model
from models.base_model import BaseModel
from datetime import datetime, time
import unittest


class Test_BaseModel_Documentation(unittest.TestCase):
    """Contains tests for the doc strings in BaseModel"""

    def test_module_docs(self):
        """Checks for documentation in base_model module"""
        self.assertGreaterEqual(len(BaseModel.__doc__), 1)

    def test_class_docs(self):
        """Checks for documentation in BaseClass"""
        self.assertGreaterEqual(len(BaseModel.__doc__), 1)

    def test_init_docs(self):
        """Checks for documentation of __init__ method"""
        self.assertGreaterEqual(len(BaseModel.__init__.__doc__), 1)

    def test_str_docs(self):
        """Checks for documentation of __str__ method"""
        self.assertGreaterEqual(len(BaseModel.__str__.__doc__), 1)

    def test_save_docs(self):
        """Checks for documentation of save() method"""
        self.assertGreaterEqual(len(BaseModel.save.__doc__), 1)

    def test_to_dict_docs(self):
        """Checks for documentation of to_dict() method"""
        self.assertGreaterEqual(len(BaseModel.to_dict.__doc__), 1)

class Test_BaseModel(unittest.TestCase):
    """Checks initializing"""

    def test_init(self):
        """Checks to see the object is created"""
        obj = BaseModel()
        self.assertIsNotNone(obj)

class Test_BaseModel_Attributes(unittest.TestCase):
    """Tests the attributes in BaseModel"""

    def test_id(self):
        """Checks UUID's of BaseModel"""

        obj = BaseModel()
        self.assertIsNotNone(obj.id)
        obj.id = 5
        self.assertEqual(obj.id, 5)

        o1 = BaseModel()
        o2 = BaseModel()
        self.assertNotEqual(o1.id, o2.id)

    def test_created_at(self):
        """Checks BaseMode.created_at"""
        obj = BaseModel()
        self.assertIsNotNone(obj.created_at)
        obj.created_at = "Created"
        self.assertEqual(obj.created_at, "Created")

    def test_created_at_format(self):
        """Checks that created_at is ISO format"""
        o = BaseModel()
        self.assertTrue(o.created_at.fromisoformat(str(o.created_at)))

    def test_updated_at(self):
        """Checks BaseModel.updated_at"""
        o = BaseModel()
        self.assertIsNotNone(o.updated_at)
        o.updated_at = "Now"
        self.assertEqual(o.updated_at, "Now")

    def test_updated_at_format(self):
        """Checks that updated_at is ISO format"""
        o = BaseModel()
        self.assertTrue(o.updated_at.fromisoformat(str(o.updated_at)))

class Test_Multiple_Instances(unittest.TestCase):
    def test_two_instances(self):
        """Checks for proper function with
        two instances of BaseModel"""
        i1 = BaseModel()
        i2 = BaseModel()
        self.assertIsInstance(i1, BaseModel)
        self.assertIsInstance(i2, BaseModel)
        self.assertTrue(hasattr(i1, "id"))
        self.assertTrue(hasattr(i1, "created_at"))
        self.assertTrue(hasattr(i1, "updated_at"))
        self.assertTrue(hasattr(i2, "id"))
        self.assertTrue(hasattr(i2, "created_at"))
        self.assertTrue(hasattr(i2, "updated_at"))
        self.assertNotEqual(i1.id, i2.id)
        self.assertNotEqual(i1.created_at, i2.created_at)
        self.assertNotEqual(i1.updated_at, i2.updated_at)
        self.assertIsInstance(i1.id, str)
        self.assertIsInstance(i1.created_at, object)
        self.assertIsInstance(i1.updated_at, object)
        self.assertIsInstance(i2.id, str)
        self.assertIsInstance(i2.created_at, object)
        self.assertIsInstance(i2.updated_at, object)

class TestBaseModelMethods(unittest.TestCase):
    """Checks methods implemented in BaseModel"""

    def test__str__(self):
        """Checks __str__() method"""
        obj = BaseModel()
        self.assertEqual(obj.__str__(), (f"[{obj.__class__.__name__}] "
                                       f"({obj.id}) {obj.__dict__}"))

    def test_to_dict(self):
        """Checks to_dict() method"""
        o = BaseModel()
        self.assertIsInstance(o.to_dict(), dict)

#Add cases for the save method to be created

if __name__ == '__main__':
    unittest.main()
