#!/usr/bin/env python3
"""
Type-annotated function that takes values and returns a tuple
"""
from typing import Union, Tuple


# Give a type hint to the tuple that will be returned
def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Parameters:
    k (str) --> string value (first element of the tuple)
    v (int / float) --> int / float value

    Returns:
    Tuple --> Values: (k(str), v(square value))
    """
    value2 = v * v
    return (k, value2)
