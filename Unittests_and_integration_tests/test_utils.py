#!/usr/bin/env python3
""" Test Utils Unittest Module """
import unittest
from parameterized import parameterized, param
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Format: Argument, Path, Output """
    @parameterized.expand([
        param({"a": 1}, ("a",), 1),
        param({"a": {"b": 2}}, ("a",), {"b": 2}),
        param({"a": {"b": 2}}, ("a", "b",), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ Test Access Nested Map Function Test """
        test_result = access_nested_map(nested_map, path)
        self.assertEqual(test_result, expected_result)
    
    @parameterized.expand([
        param({}, ("a",), {}),
        param({"a": 1}, ("a", "b",), 1),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_result):
        with self.assertRaises(KeyError):
            test_result = access_nested_map(nested_map, path)
            raise KeyError("Failed: KeyError")


if __name__ == '__main__':
    unittest.main()