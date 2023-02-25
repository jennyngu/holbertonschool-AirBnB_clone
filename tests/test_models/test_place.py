#!/usr/bin/python3
"""
Unittest for BaseModel([...])
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_id(self):
        p = Place()
        self.assertEqual(p.number_rooms, 0)
