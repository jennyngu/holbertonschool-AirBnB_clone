#!/usr/bin/python3
"""
Unittest for BaseModel([...])
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def test_id(self):
        b = BaseModel()
        self.assertEqual(type(b.id), str)

    def test_str(self):
        b = BaseModel()
        expected_str = b.__str__()
        self.assertEqual(b.__str__(), expected_str)

    def test_save(self):
        b = BaseModel()
        before_save = b.updated_at
        b.save()
        after_save = b.updated_at
        self.assertNotEqual(before_save, after_save)

    def test_to_dict(self):
        b = BaseModel()
        b.name = "First Model"
        b.my_number = 10
        b.save()
        expected_dict = {
            'id': b.id,
            'name': 'First Model',
            'my_number': 10,
            'created_at': b.created_at.isoformat(),
            'updated_at': b.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(b.to_dict(), expected_dict)

    def test_created_at(self):
        b = BaseModel()
        self.assertEqual(type(b.created_at), datetime)
