#!/usr/bin/python3
"""Test Module
    """

import unittest
import pep8
from models.place import Place


class TestPlace(unittest.TestCase):
    """[summary]

    Args:
        unittest ([type]): [description]
    """

    def test_pep8(self):
        """test pep8
            """
        style = pep8.StyleGuide()
        pep8_check = style.check_files(["models/place.py"])
        self.assertEqual(pep8_check.total_errors, 0)

    def test_doc(self):
        """Documentation test
        """
        self.assertIsNotNone(Place.__doc__)

class PlaceTest(unittest.TestCase):
    def  setUp(self):
        """
        objects for testing
        """
        self.testing = Place()
        self.testing2 = Place()

    def test_instantiation(self):
        """
        class attributes initialization testing
         """
        self.assertIsInstance(self.testing, Place)
        self.assertIsInstance(self.testing2, Place)
        self.assertTrue(hasattr(self.testing, "name"))
        self.assertTrue(hasattr(self.testing2, "user_id"))
        self.assertTrue(hasattr(self.testing, "city_id"))
        self.assertTrue(hasattr(self.testing2, "latitude"))
        self.assertTrue(hasattr(self.testing, "latitude"))
        self.assertTrue(self.testing.id != self.testing2.id)

    def test_types(self):
        """
        isntance attribute
        """
        self.assertEqual(self.testing.name, "")
        self.assertTrue(type(self.testing.city_id) is str)
        self.assertTrue(type(self.testing.user_id) is str)
        self.assertTrue(type(self.testing.description) is str)
        self.assertTrue(type(self.testing.longitude) is float)
        self.assertTrue(type(self.testing.latitude) is float)


if __name__ == "__main__":
    unittest.main()
