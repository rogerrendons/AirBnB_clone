#!/usr/bin/python3
"""Test Module
    """

import unittest
import pep8
from models.user import User


class TestUser(unittest.TestCase):
    """
    Args:
        unittest ([type]): [description]
    """

    def test_pep8(self):
        """test pep8
        """
        style = pep8.StyleGuide()
        pep8_check = style.check_files(["models/user.py"])
        self.assertEqual(pep8_check.total_errors, 0)

    def test_doc(self):
        """Documentation test
        """
        self.assertIsNotNone(User.__doc__)

    def  setUp(self):
        """
        	test
        """
        self.testing = User()

    def test_instantiation(self):
        """class test"""
        self.assertIsInstance(self.testing, User)
        self.assertTrue(hasattr(self.testing, "first_name"))
        self.assertTrue(hasattr(self.testing, "last_name"))
        self.assertTrue(hasattr(self.testing, "email"))

    def test_types(self):
        """attributes str"""
        self.assertTrue(type(self.testing.first_name) is str)
        self.assertTrue(type(self.testing.last_name) is str)
        self.assertTrue(type(self.testing.email) is str)

if __name__ == "__main__":
    unittest.main()
