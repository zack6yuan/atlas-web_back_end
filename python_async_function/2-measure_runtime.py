#!/usr/bin/env python3
"""
A measure time function that measures execution time
"""
import async
import random
import time


async def measure_time(n: int, max_delay: int) -> float:
    """
    Parameters:
    n (integer) --> measures execution time
    max_delay (integer) --> 

    Returns:
    total_time / n (float)
    """
    