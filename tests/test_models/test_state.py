#!/usr/bin/python3
"""Test Module
    """

import unittest
import pep8
from models.state import State


class TestState(unittest.TestCase):
    """[summary]

    Args:
        unittest ([type]): [description]
    """

    def test_pep8(self):
        """test pep8
            """
        style = pep8.StyleGuide()
        pep8_check = style.check_files(["models/state.py"])
        self.assertEqual(pep8_check.total_errors, 0)

    def test_doc(self):
        """Documentation test
        """
        self.assertIsNotNone(State.__doc__)

class StateTest(unittest.TestCase):
    def  setUp(self):
        """
        objects for testing
        """
        self.testing = State()

    def test_instantiation(self):
        """init test"""
        self.assertIsInstance(self.testing, State)
        self.assertTrue(hasattr(self.testing, "name"))

    def test_types(self):
        """instance attributes are str type"""
        self.assertTrue(type(self.testing.name) is str)

if __name__ == "__main__":
    unittest.main()
