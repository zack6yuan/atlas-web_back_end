#!/usr/bin/env python3
""" Test Utils Unittest Module """
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b",), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        test_result = access_nested_map(nested_map, path)
        self.assertEqual(test_result, expected_result)
        

if __name__ == '__main__':
    unittest.main()
