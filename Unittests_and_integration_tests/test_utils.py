#!/usr/bin/env python3
"""Test utils.py"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestGetJson(unittest.TestCase):
    """Test get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """uses @parameterized.expand to test different inputs"""
        self.assertEqual(get_json(test_url), test_payload)


if __name__ == '__main__':
    unittest.main()
