#!/usr/bin/env python3
""" Test Client Module """
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class, param
from typing import Dict
from client import GitHubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Test GitHub Org Client Class """
    @parameterized.expand([
        param('google'),
        param('abc'),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get):
        """ Test Org Function """
        client_instance = GitHubOrgClient(org_name)
        test_result = client_instance.org()
        self.assertEqual(test_result,)
        
        
        
        
        
        
    def test_public_repos_url(self):
        """ Test Public Repos Function """
        with patch('client.GithubOrgClient', new_callable = PropertyMock) as mock_obj:
            
        
    
    @parameterized.expand([
        param({"liscense": {"key": "my_liscense"}}, "my_liscense", True),
        param({"liscense": {"key": "other_liscense"}}, "my_liscense", False),
    ])
    def test_has_license(self, repo: Dict[str, Dict], liscense_key: str, expected_result):
        output = GithubOrgClient.has_license(repo, liscense_key)
        self.assertEqual(output, expected_result)
    
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Test Integration GitHub Org Client Class """
    @parameterized_class(
        "org_payload",
        "repos_payload",
        "expected_repos",
        "apache2_repos"
    )
    def setUpClass(self):
        """ Set Up Class Function """
        pass
    
    def tearDownClass(self):
        """ Tear Down Class Function """
        pass





if __name__ == '__main__':
    unittest.main()