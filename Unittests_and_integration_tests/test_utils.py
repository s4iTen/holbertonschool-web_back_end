#!/usr/bin/env python3
"""get_json function"""
import unittest
from unittest.mock import Mock, patch
from utils import get_json, memoize
from parameterized import parameterized


class TestGetJson(unittest.TestCase):
    """Test cases for the get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test Get JSON Method"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Test case for the memoize decorator"""

    class TestClass:
        """Test class with memoized method"""

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self):
        """Test memoization of a_property"""
        test_instance = self.TestClass()
        with patch.object(test_instance, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42
            result1 = test_instance.a_property()
            result2 = test_instance.a_property()
            mock_a_method.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
