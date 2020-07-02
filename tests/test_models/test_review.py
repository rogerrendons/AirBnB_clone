#!/usr/bin/python3
"""Test Module
    """

import unittest
import pep8
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """[summary]

    Args:
        unittest ([type]): [description]
    """

    def test_pep8(self):
        """test pep8
            """
        style = pep8.StyleGuide()
        pep8_check = style.check_files(["models/review.py"])
        self.assertEqual(pep8_check.total_errors, 0)

    def test_doc(self):
        """Documentation test
        """
        self.assertIsNotNone(Review.__doc__)

    def setUp(self):
        """
        	Test
        """
        self.testing = Review()
        self.testing2 = Review()

    def test_instantiation(self):
        """
        	Attr test
        """
        self.assertIsInstance(self.testing, Review)
        self.assertIsInstance(self.testing2, Review)
        self.assertTrue(hasattr(self.testing, "place_id"))
        self.assertTrue(hasattr(self.testing, "user_id"))
        self.assertTrue(hasattr(self.testing, "text"))

    def test_reinstantiation(self):
        testing3 = self.testing.created_at
        testing4 = self.testing2.created_at
        self.assertTrue(testing3 != testing4)
        self.assertTrue(type(testing3) is datetime.datetime)

    def test_types(self):
        """
        	attributes str type
        """
        self.assertTrue(type(self.testing.place_id) is str)
        self.assertTrue(type(self.testing.user_id) is str)

if __name__ == "__main__":
    unittest.main()
