#!/usr/bin/env python3
""" Test Utils Module """
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ 
    Test class for access nested map
    Inherits from unittest.TestCase
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b",), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Access nested map test
        Arguments:
            self --> instance of the class
            nested_map --> dictionary
            path --> keys representing the path
            expected_result --> value expected to be returned
        Methods:
            Calls access_nested_map with the map and path
            Uses assertEqual to compare results
        """
        test_result = access_nested_map(nested_map, path)
        self.assertEqual(test_result, expected_result)
    
    """ Allow multiple test cases """
    @parameterized.expand([
        ({}, ("a",), {}),
        ({"a": 1}, ("a", "b",), 1),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Access nested map exception test
        Arguments:
            self --> instance of the class
            nested_map --> dictionary
            path --> keys representing the path
        Methods
             assertRaises --> check if a KeyError is raised
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
            
class TestGetJson(unittest.TestCase):
    """
    TestGetJson Class
    Inherits fron unittest.TestCase
    """
    """ Allow multiple test cases """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Function to test get_json
        Arguments:
            self --> instance of the class
            test_url --> URL passed to get_json
            test_payload --> Mocked json data
            mock_get --> requests.get mock object
        Methods:
            @patch: decorator --> replace requests.get with mock object
            Create a new Mock object
        Returns:
            The mock response
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        
        test_result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(test_result, test_payload)
        
class TestMemoize(unittest.TestCase):
    """
    Test Memoize Class
    Inherits from unittest.TestCase
    """
    def test_memoize(self):
        """
        Memoize Test
        Arguments:
            self --> instance of the class
        """
        class TestClass:
            """ Inner Class "TestClass" """
            def a_method(self):
                """
                a_method
                Arguments:
                    self --> instance of the class
                Returns:
                    42
                """
                return 42
            
            @memoize
            def a_property(self):
                """
                a_property
                Arguments;
                    self --> instnace of the class
                Returns:
                    a_method()
                """
                return self.a_method()
        
        """ patch.object --> format: (object, atrribute) """
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