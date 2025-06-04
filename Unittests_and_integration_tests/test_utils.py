#!/usr/bin/env python3
""" Test utils module """
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized, param
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Test class for access nested map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b",), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ Access nested map test """
        test_result = access_nested_map(nested_map, path)
        self.assertEqual(test_result, expected_result)
        
    @parameterized.expand([
        ({}, ("a",), {}),
        ({"a": 1}, ("a", "b",), 1),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_result):
        """ Access nested map exception test """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
            
class TestGetJson(unittest.TestCase):
    """ TestGetJson Class
    Inherits fron unittest.TestCase """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ Test Get Json and ensure that the function returns a Mock obeject """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        
        test_result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(test_result, test_payload)
        
class TestMemoize(unittest.TestCase):
    """ Test Memoize Class """
    def test_memoize(self):
        """ Memoize Test """
        class TestClass:

            def a_method(self):
                return 42
            
            @memoize
            def a_property(self):
                return self.a_method()
        
        """
        patch.object --> format: (object, atrribute)
        """
        with patch.object(TestClass, 'a_method') as mock_obj:
            """
            Methods:
            Create instance of test class and call a_property twice
            Verify that a_method is called once using assert_called_once
            """
            instance = TestClass()
            instance.a_property()
            instance.a_property()
            
            mock_obj.assert_called_once()
            
            
if __name__ == '__main__':
    unittest.main()