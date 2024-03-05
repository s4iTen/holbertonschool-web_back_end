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
    def test_memoize(self):
        """Test Memoize Method"""
        class TestClass:
            """Test class with memoized method"""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            test_class = TestClass()
            real_return = test_class.a_property
            real_return = test_class.a_property

            self.assertEqual(real_return, 42)
            mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
