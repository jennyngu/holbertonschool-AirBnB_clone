#!/usr/bin/python3
"""
Unittest for BaseModel([...])
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_id(self):
        r = Review()
        self.assertEqual(r.text, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.place_id, "")
