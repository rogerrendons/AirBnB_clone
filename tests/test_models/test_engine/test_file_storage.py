#!/usr/bin/python3
"""Test Module
    """

import unittest
import pep8
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """[summary]

    Args:
        unittest ([type]): [description]
    """

    # def test_pep8(self):
    #     """test pep8
    #         """
    #     style = pep8.StyleGuide()
    #     pep8_check = style.check_files(["/home/holberton/AirBnB_clone/models/engine/file_storage.py"])
    #     self.assertEqual(pep8_check.total_errors, 0)

    # def test_doc(self):
    #     """Documentation test
    #     """
    #     self.assertIsNotNone(FileStorage.__doc__)
    #     self.assertIsNotNone(FileStorage.all.__doc__)
    #     self.assertIsNotNone(FileStorage.new.__doc__)
    #     self.assertIsNotNone(FileStorage.save.__doc__)
    #     self.assertIsNotNone(FileStorage.reload.__doc__)


if __name__ == "__main__":
    unittest.main()
