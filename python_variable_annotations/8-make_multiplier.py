#!/usr/bin/env python3
"""
Type-annotated function that takes a float
Returns a function taht multiplies a float by multiplier
"""
from typing import Union


def make_multiplier(multiplier: float):
    """
    Parameters:
    multiplier (float) --> float value

    Returns:
    New Function that multiples a float by multiplier
    """