#!/usr/bin/env python3
"""unit tests for client """
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Testcases for GithubOrgClient function"""

    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_payload, mock_get_json):
        """Test GithubOrgClient.org returns the correct value"""
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with
        (f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected_payload)

    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test GithubOrgClient._public_repos_url returns the correct value"""
        expected_repos_url = "https://api.github.com/orgs/test_org/repos"
        mock_org.return_value = {"repos_url": expected_repos_url}

        client = GithubOrgClient("test_org")
        result = client._public_repos_url

        self.assertEqual(result, expected_repos_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos returns
        the correct list of repos"""
        repos_name = [
            {"name": "repo1"},
        ]
        mock_get_json.return_value = repos_name
        expected_repo = ["repo1"]
        public_repo_url = "example.com"

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = public_repo_url

            client = GithubOrgClient("test_org")
            result = client.public_repo()

            self.assertEqual(result, expected_repo)
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(public_repo_url)


if __name__ == '__main__':
    unittest.main()
