#!/usr/bin/env python3
"""
Type-annotated function that takes a float
Returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Parameters:
    multiplier (float) --> float value
    value (float) --> input value
    
    Method:
    Define inner function for math operations
    Use Callable[[], ] type hint for clarity...
    Takes in float, returns float

    Returns:
    New Function that multiples a float by multiplier
    """
    def float_multiplier(value: float) -> float:
        """
        Parameters:
        value (float) -> value to be multiplied
        
        Method:
        Retrieve the product of value and multiplier
        Return value according to format (float)

        Returns:
        Result of the operation (float)
        """
        return value * multiplier

    return float_multiplier
