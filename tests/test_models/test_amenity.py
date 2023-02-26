#!/usr/bin/python3
"""
Unittest for Amenity([...])
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_id(self):
        a = Amenity()
        self.assertEqual(a.name, "")
