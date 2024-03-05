#!/usr/bin/env python3
"""Test Client File"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for the GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self):
        """Test Org Method"""
        test_org = "example_org"
        with patch('client.get_json') as mock_get_json:
            client = GithubOrgClient(test_org)
            client.org()
            mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{test_org}")


if __name__ == "__main__":
    unittest.main()
