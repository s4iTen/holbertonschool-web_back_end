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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected) -> None:
        """Test Has License Method"""
        test_client = GithubOrgClient(repo)
        result = test_client.has_license(license_key)
        self.assertEqual(result, expected)

    @patch("client.get_json", return_value=[{"name": "holberton"}])
    def test_public_repos(self, mock_get_json):
        """Test Public Repos Method"""

        expected_payload = [{"name": "repo1"}, {"name": "repo2"}]

        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value='https://api.github.com/'
                          ) as mock_url:
            test_client = GithubOrgClient("holberton")
            result = test_client.public_repos()
            self.assertEqual(result, expected_payload)
            mock_url.assert_called_once()
            mock_get_json.assert_called_once()

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


if __name__ == "__main__":
    unittest.main()
