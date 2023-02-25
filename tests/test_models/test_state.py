#!/usr/bin/python3
"""
Unittest for State([...])
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_id(self):
        s = State()
        self.assertEqual(s.name, "")
