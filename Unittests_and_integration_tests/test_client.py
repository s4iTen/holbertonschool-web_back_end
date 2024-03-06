#!/usr/bin/env python3
"""Test Client File"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """Test Public Repos Url Method"""
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock,
                          return_value={'repos_url': 'holberton'}
                          ) as mock_org:
            test_json = {"repos_url": 'holberton'}
            test_client = GithubOrgClient(test_json.get("repos_url"))
            test_return = test_client._public_repos_url
            mock_org.assert_called_once
            self.assertEqual(
                test_return,
                mock_org.return_value.get("repos_url"))

    @patch("client.get_json", return_value=[{"name": "holberton"}])
    def test_public_repos(self, mock_get_json):
        """Test Public Repos Method"""
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value='https://api.github.com/'
                          ) as mock_url:
            test_client = GithubOrgClient("holberton")
            test_return = test_client.public_repos()
            self.assertEqual(test_return, [{"name": "holberton"}])
            mock_url.assert_called_once()
            mock_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
