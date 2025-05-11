#!/usr/bin/env python3
"""
Type-annotated function that takes a list of integers and returns sum as float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Parameters:
    mxd_list (list(int + float)) --> list of integers and floats
    
    Methods:
    To take in multiple types, use Union
    Use the sum() function to retrieve the sum
    of the mixed list (different types)

    Returns:
    The sum of the list as a float
    """
    return (sum(mxd_lst))
