#!/usr/bin/python3
"""
Unittest for User([...])
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_id(self):
        u = User()
        self.assertEqual(u.email, "")
        self.assertEqual(u.password, "")
        self.assertEqual(u.first_name, "")
        self.assertEqual(u.last_name, "")
