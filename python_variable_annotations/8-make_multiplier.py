#!/usr/bin/env python3
from typing import Callable
"""
Type-annotated function that takes a float
Returns a function that multiplies a float by multiplier
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Parameters:
    multiplier (float) --> float value
    value (float) --> input value

    Returns:
    New Function that multiples a float by multiplier
    """
    def float_multiplier(value: float) -> float:
        """
        Parameters:
        value (float) -> value to be multiplied

        Returns:
        Result of the operation
        """
        return value * multiplier

    return float_multiplier
