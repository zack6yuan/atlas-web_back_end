#!/usr/bin/env python3
""" Test Client Module """
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """ Test GitHub Org Client Class """
    def test_org(self):
        """ Test Org Function """
        pass
    
    @parameterized.expand([
        ({"liscense": {"key": "my_liscense"}}, "my_liscense", True),
        ({"liscense": {"key": "other_liscense"}}, "my_liscense", False),
    ])
    def test_has_license(self):
        pass
    
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