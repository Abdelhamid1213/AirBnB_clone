#!/usr/bin/python3
"Unit tests for BaseModel class"
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    "Unit tests suite for BaseModel class"

    def test_save(self):
        "Tests that save method updates the datetime"
        base = BaseModel()
        old_time = base.updated_at
        base.save()
        self.assertNotEqual(old_time, base.updated_at)

    def test_to_dict(self):
        """
        Tests that to_dict:
            - returns a dictionary
            - that contains all keys/values of __dict__
            - contains __class__ and that this __class__ is the class name
        """
        base = BaseModel()

        "Returns a dictionary"
        returned_dict = base.to_dict()
        self.assertIsInstance(returned_dict, dict)

        "Dictionary contains all keys/values of __dict__"
        default_dict = base.__dict__
        self.assertTrue(default_dict.items() <= returned_dict.items())

        "Dictionary contains __class__, which is the class name"
        self.assertTrue("__class__" in returned_dict)
        self.assertEqual(returned_dict["__class__"], type(base).__name__)

    def test_str(self):
        "Tests that the string representation has the right format"
        base = BaseModel()
        right_format = f"[{type(base).__name__}] ({base.id}) {base.__dict__}"
        self.assertEqual(str(base), right_format)
