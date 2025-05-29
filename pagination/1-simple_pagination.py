#!/usr/bin/env python3
"""
Simple helper function
"""
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple:
    """
    Arguments:
        page (int) --> pagination parameter
        page_size (int) --> pagination parameter
    Methods:
        Use start index and end index to handle pagination
    Returns:
        A tuple of the start and end indexes
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Arguemnts:
            page --> the current page
            page_size --> the size of the page
        Methods:
            Verify integer types and values
            self.dataset() --> access the full dataset / read csv file
            Call the index_range function with page and page size
            Check if arguments are in range for the dataset
        Returns:
            The dataset
        """
        assert isinstance(page, int) and (page > 0)
        assert isinstance(page_size, int) and (page_size > 0)

        page_data = self.dataset()

        start, end = index_range(page, page_size)

        if (start > len(page_data)):
            return []

        final_data = [page_data[0], page_data[1], page_data[3], page_data[4]]
        return final_data
