#!/usr/bin/env python3
"""
Type-annotated function that takes a float
Returns a function that multiplies a float by multiplier
""" 


def make_multiplier(multiplier: float): # Callable
    """
    Parameters:
    multiplier (float) --> float value

    Returns:
    New Function that multiples a float by multiplier
    """
    def getNumber()