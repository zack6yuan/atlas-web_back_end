#!/usr/bin/env python3
""" Client Testing Module """
import unittest
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from utils import get_json
import client
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Test GithubOrgClient Class
    Inherits from unittest.TestCase
    """
    """ Allow multiple test cases """
    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get):
        """
        Test Org Function
        Arguments:
            org_name --> name of the organization
        Methods:
            Create new client instance
            assert_called_once_with --> assert called once
        """
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
        Test Public Repos Function
        Arguments:
            self --> instnace of the class
            mock_json --> mock json method
        """
        mock_json.return_value = [{"name": "Tesla"}]
        
        """
        Methods:
            PropertyMock --> used to mock @property attributes
        """
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as TestMock:
            TestMock.return_value = {"repos_url": "https://api.github.com/orgs/github_client/repos"}
            
        github_client = GithubOrgClient('Tesla')
        value = github_client.public_repos()
        
        mock_json.assert_called_once()
        self.assertEqual(result, ["Tesla"])

    """ Allow multiple test cases """
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Test Has License
        Arguments:
            self --> instance of the class
            license_key --> license identifier (key)
            expected_result --> return value to compare to
        """
        output = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(output, expected_result)
        
""" Add parameters to entire test class """
@parameterized_class([
    {'org_payload': {}, 'repos_payload': {}, 'expected_repos': {}, 'apache2_repos': {}}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Test Integration Github Org Client Class
    Inherits from unittest.TestCase
    """
    @classmethod
    def setUpClass(self):
        """
        setUp class function
        Arguments:
            self --> instance of the class
        Methods:
            Starts a patcher
        """
        self.patcher = patch('requests.get')
        self.mock = self.patcher.start()
    
    @classmethod
    def tearDownClass(self):
        """
        tearDown class function
        Arguments:
            self --> instance of the class
        Methods:
            Stops the patcher
        """
        self.patcher.stop()
        

if __name__ == '__main__':
    unittest.main()