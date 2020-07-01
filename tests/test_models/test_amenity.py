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


class TestAmenity(unittest.TestCase):
    """[summary]

    Args:
        unittest ([type]): [description]
    """

    def test_pep8(self):
        """test pep8"""
        style = pep8.StyleGuide()
        pep8_check = style.check_files(["models/amenity.py"])
        self.assertEqual(pep8_check.total_errors, 0)

    def test_doc(self):
        """Documentation test
        """
        self.assertIsNotNone(Amenity.__doc__)


if __name__ == "__main__":
    unittest.main()
