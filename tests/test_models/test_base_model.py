#!/usr/bin/python3
"""Test Module
    """

import unittest
import pep8
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import datetime


class TestBaseModel(unittest.TestCase):
    """[summary]

    Args:
        unittest ([type]): [description]
    """

    def test_pep8(self):
        """test pep8"""
        style = pep8.StyleGuide()
        pep8_check = style.check_files(["models/base_model.py"])
        self.assertEqual(pep8_check.total_errors, 0)

    def test_doc(self):
        """Documentation test"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

class BaseModelTest(unittest.TestCase):
    def  setUp(self):
        """objects to be tested"""
        self.testing = BaseModel()
        self.testing2 = BaseModel()

    def test_instantiation(self):
        """BaseModel class"""
        self.assertIsInstance(self.testing, BaseModel)
        self.assertIsInstance(self.testing2, BaseModel)
        self.assertTrue(hasattr(self.testing, "id"))
        self.assertTrue(hasattr(self.testing, "__class__"))
        self.assertTrue(hasattr(self.testing, "created_at"))
        self.assertTrue(self.testing.id != self.testing2.id)

    def test_reinstantiation(self):
        model1_ctime = self.testing.created_at
        model2_ctime = self.testing2.created_at
        self.assertTrue(model1_ctime != model2_ctime)
        self.assertTrue(type(model1_ctime) is datetime.datetime)

if __name__ == "__main__":
    unittest.main()
