#!/usr/bin/python3
"""
Unittest for City([...])
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_id(self):
        c = City()
        self.assertEqual(c.name, "")
