#!/usr/bin/env python3
"""
Coroutine that collects 10 random numbers, then returns the numbers
"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Parameters: None

    Methods:
    async for --> loop over asynchronous items

    Returns:
    The list of delays
    """
    return [x async for x in async_generator()]
