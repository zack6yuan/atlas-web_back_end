#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ init method """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        Methods:
            Checks that the dataset holds no value
            Opens the CSV file
            Creates a reader object
            Creates a new list [index 1 to the end]
        Returns:
            The dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0
        Methods:
            Checks if the dataset has no value assigned to it
            The result of self.dataset() is stored in "dataset"
            Slices the list
            Dictionary comprehension
        Returns:
            The dictionary (indexed_dataset)
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get Hyper Index Function
        Arguments:
            index --> the starting point for the page
            page_size --> the number of items on the page
        Methods:
            Check if page_size is an integer (assert)
            Check is page_size is > 0 (assert)
            Retrieve the dataset and assign to new_dataset
            Add two to the index provided (next_index)
        Errors:
            AssertionError raised it index >- len(new_dataset)
        Returns:
            A dictionary with key-value pairs according to format
        """
        assert isinstance(page_size, int)
        assert page_size > 0

        new_dataset = self.indexed_dataset()
        next_index = index + 2

        if index >= len(new_dataset):
            raise AssertionError

        return {
            "index": index,
            "data": new_dataset,
            "page_size": page_size,
            "next_index": next_index,
        }
