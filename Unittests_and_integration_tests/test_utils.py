#!/usr/bin/env python3
""" Test Utils Unittest Module """
import Unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a ",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b",), {"b": 2}),
    ])
    def TestAccessNestedMap.test_access_nested_map(self, nested_map, path):
        test1 = access_nested_map({"a": 1}, ("a",))
        test2 = access_nested_map({"a": {"b": 2}}, ("a ",))
        test3 = access_nested_map({"a": {"b": 2}}, ("a", "b",))
        