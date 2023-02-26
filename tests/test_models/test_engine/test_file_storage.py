#!/usr/bin/python3
"""
Unittest for FileStorage([...])
"""
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models.user import User
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

    def test_all(self):
        f = FileStorage()
        all_objs = f.all()
        self.assertIsNotNone(all_objs)
        self.assertEqual(dict, type(all_objs))
        self.assertIs(all_objs, f._FileStorage__objects)

    def test_new(self):
        user = User()
        self.storage.new(user)
        key = f"{user.__class__.__name__}.{user.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        f = FileStorage()
        f.save()
        self.assertTrue(os.path.exists("file.json"))

    def setUp(self):
        self.storage = FileStorage()
        self.storage.save()

    def tearDown(self):
        os.remove("file.json")

    def test_reload(self):
        user = User()
        self.storage.new(user)
        self.storage.save()
        self.storage.reload()
        key = f"{user.__class__.__name__}.{user.id}"
        self.assertIn(key, self.storage.all())
