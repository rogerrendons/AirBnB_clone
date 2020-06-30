#!/usr/bin/python3
"""Test Module
    """

import unittest
import pep8


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


if __name__ == "__main__":
    unittest.main()
