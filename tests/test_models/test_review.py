#!/usr/bin/python3
"""Test Module
    """

import unittest
import pep8
from models.review import Review


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


if __name__ == "__main__":
    unittest.main()
