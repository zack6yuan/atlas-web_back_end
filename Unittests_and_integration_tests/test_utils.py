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
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b",), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected_result):
        """ Test Access Nested Map Function Test """
        test_result = access_nested_map(nested_map, path)
        self.assertEqual(test_result, expected_result)
    
    # Complete, checker did not give points
    @parameterized.expand([
        ({}, ("a",), {}),
        ({"a": 1}, ("a", "b",), 1),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping, path: Sequence, expected_result):
        """ Test Access Nested Map Exception Test
            Inherits fron unittest.TestCase """
        with self.assertRaises(KeyError):
            test_result = access_nested_map(nested_map, path)
            raise KeyError("Failed: KeyError")



if __name__ == '__main__':
    unittest.main()