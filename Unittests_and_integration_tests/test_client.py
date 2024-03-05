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
    def test_org(self, org_name, mock_get_json):
        """Test the org method"""
        with patch("client.get_json", mock_get_json):
            client = GithubOrgClient()
            self.assertEqual(client.org(org_name), mock_get_json())


if __name__ == "__main__":
    unittest.main()