#!/usr/bin/python3
"""Test Module
    """

import unittest
import pep8
from models.city import City


class TestCity(unittest.TestCase):
    """[summary]

    Args:
        unittest ([type]): [description]
    """

    def test_pep8(self):
        """test pep8
            """
        style = pep8.StyleGuide()
        pep8_check = style.check_files(["models/city.py"])
        self.assertEqual(pep8_check.total_errors, 0)

    def test_doc(self):
        """Documentation test
        """
        self.assertIsNotNone(City.__doc__)

    def  setUp(self):
        """test"""

        self.testing = City()
        self.testing2 = City()

    def test_instantiation(self):
        """
        initialization of class attributes
        """
        self.assertIsInstance(self.testing, City)
        self.assertIsInstance(self.testing2, City)
        self.assertTrue(hasattr(self.testing, "state_id"))
        self.assertTrue(hasattr(self.testing, "name"))
        self.assertTrue(self.testing.id != self.testing2.id)

    def test_types(self):
        """
        city attributes
        """
        self.assertTrue(type(self.testing.state_id) is str)
        self.assertTrue(type(self.testing.name) is str)

if __name__ == "__main__":
    unittest.main()
