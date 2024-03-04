#!/usr/bin/env python3
"""Test utils.py"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function"""
    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map, path, expected_exception):
        """uses @parameterized.expand to test different inputs"""
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    unittest.main()
