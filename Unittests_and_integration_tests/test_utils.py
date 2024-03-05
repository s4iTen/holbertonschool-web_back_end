#!/usr/bin/env python3
"""get_json function"""
import unittest
from unittest.mock import patch, Mock
import utils


class TestGetJson(unittest.TestCase):
    """Test cases for the get_json function"""
    @patch('your_module.utils.requests.get')
    def test_get_json(self, mock_get):
        # Define test cases with input parameters and expected results
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]

        for test_url, test_payload in test_cases:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            result = utils.get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)
            mock_get.reset_mock()

if __name__ == '__main__':
    unittest.main()
