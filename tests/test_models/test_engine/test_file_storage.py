#!/usr/bin/python3
"""
Unittest for FileStorage([...])
"""
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import unittest
import os


class TestFileStorage(unittest.TestCase):
    def test__file_path(self):
        b = BaseModel()
        f = FileStorage()

        self.assertEqual(type(b.id), str)

    def test_str(self):
        b = BaseModel()
        expected_str = b.__str__()
        self.assertEqual(b.__str__(), expected_str)

    def test_save(self):
        f = FileStorage()
        f.save()
        self.assertTrue(os.path.exists("file.json"))

    def setUp(self):
        b = BaseModel()
        b.save()

    def tearDown(self):
        os.remove("file.json")

    def test_reload(self):
        f = FileStorage()
        f.reload()
        self.assertTrue(len(storage.all()) > 0)
