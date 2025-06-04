#!/usr/bin/env python3
""" Client testing module """
import unittest
from unittest.mock import Mock, patch
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """ Test github org client class """
    @parameterized.expand([
        param('google'),
        param('abc'),
    ])
    @patch('client.get_json')
    def test_org(self, mock_get):
        """ Test org function """
        
        
        
        
        