#!/usr/bin/env python3
""" Client testing module """
import unittest
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized, param, parameterized_class
from client import GithubOrgClient
from utils import get_json
import client
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ Test github org client class """
    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get):
        """ Test Org Function """
        client_instance = GithubOrgClient(org_name)
        test_result = client_instance.org()
        mock_get.assert_called_once_with("https://api.github.com/orgs/{}".format(org_name))

    @patch('client.get_json')
    def test_public_repos_url(self, mock_json):
        """
        Methods:
            @patch: decorator --> replace get_json with mock object
            mock_json --> creates a mock object, used as argument
            mock_json.return_value --> set the value of the mocked get_json function
            test_case(mocked_org) = new instnace of GithubOrgClient
            assert that the value is the same as the repo name
        """
        mock_json.return_value = [{"name": "repo_name"}]
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as NewMock:
            NewMock.return_value = {"repos_url": "https://api.github.com/orgs/github_client/repos"}
            github_client = GithubOrgClient("mocked_org")
            value = github_client.public_repos()
            self.assertEqual(value, ["repo_name"])
            
    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        Methods:
        """
        mock_json.return_value = [{"name": "Tesla"}]
        
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as TestMock:
            TestMock.return_value = {"repos_url": "https://api.github.com/orgs/github_client/repos"}
            
        github_client = GithubOrgClient('Tesla')
        value = github_client.public_repos()
        
        mock_json.assert_called_once()
        self.assertEqual(result, ["Tesla"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        output = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(output, expected_result)
        
@parameterized_class([
    {'org_payload': {}, 'repos_payload': {}, 'expected_repos': {}, 'apache2_repos': {}}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Test Integration Github Org Client Class """
    @classmethod
    def setUpClass(self):
        """ set up class function """
        self.patcher = patch('requests.get')
        self.mock = self.patcher.start()
    
    @classmethod
    def tearDownClass(self):
        """ tear down class function """
        self.patcher.stop()
        

if __name__ == '__main__':
    unittest.main()