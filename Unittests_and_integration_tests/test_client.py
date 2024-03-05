#!/usr/bin/env python3
"""Test Client File"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for the GithubOrgClient class"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, test_org, mock_json):
        """Test Org Method"""
        client = GithubOrgClient(test_org)
        client.org()
        mock_json.assert_called_once_with(
            f"https://api.github.com/orgs/{test_org}")


if __name__ == "__main__":
    unittest.main()
