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
        self.assertEqual(b.save(), None)

    def test_to_dict(self):
        b = BaseModel()
        b.name = "First Model"
        b.my_number = 10
        expected_dict = b.to_dict()
        self.assertEqual(b.to_dict(), expected_dict)

    def test_created_at(self):
        b = BaseModel()
        self.assertEqual(type(b.created_at), datetime)
