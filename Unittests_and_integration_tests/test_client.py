#!/usr/bin/env python3
""" Test Client Module """
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """ Test GitHub Org Client Class """
    def test_org(self):
        """ Test Org Function """
        pass
    
    @parameterized.expand([
        ({"liscense": {"key": "my_liscense"}}, "my_liscense"),
        ({"liscense": {"key": "other_liscense"}}, "my_liscense"),
    ])
    def test_has_liscense(self):
        pass
        




if __name__ == '__main__':
    unittest.main()