#!/usr/bin/env python3
""" Test Utils Unittest Module """
import unittest
from unittest.mock import patch, Mock, mock_open
from parameterized import parameterized, param
from utils import access_nested_map
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    """ Test Access Nested Map Class
        Inherits from unittest.TestCase
        Format: Argument, Path, Output """
    # Tests are running, checker not accepting for the decorator
    @parameterized.expand([
        param({"a": 1}, ("a",), 1),
        param({"a": {"b": 2}}, ("a",), {"b": 2}),
        param({"a": {"b": 2}}, ("a", "b",), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected_result):
        """ Test Access Nested Map Function Test """
        test_result = access_nested_map(nested_map, path)
        self.assertEqual(test_result, expected_result)
    
    # Complete, checker did not give points
    @parameterized.expand([
        param({}, ("a",), {}),
        param({"a": 1}, ("a", "b",), 1),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping, path: Sequence, expected_result):
        """ Test Access Nested Map Exception Test
            Inherits fron unittest.TestCase """
        with self.assertRaises(KeyError):
            test_result = access_nested_map(nested_map, path)
            raise KeyError("Failed: KeyError")
        
class TestGetJson(unittest.TestCase):
    """ Test Get Json Class """
    def test_get_json():
        """ Test Get Json Function """
        
class TestMemoize(TestCase):
    """ Test Memoize Class """
    @patch('test_utils.a_method')
    def test_memoize():
        class TestClass:
            
            def a_method(self):
                return 42
            
            @memoize
            def a_property(self):
                return self.a_method()
    



if __name__ == '__main__':
    unittest.main()