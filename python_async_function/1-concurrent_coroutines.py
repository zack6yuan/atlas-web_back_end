#!/usr/bin/env python3
"""
Asynchronous Coroutine that takes in two integer arguments
"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Parameters:
    n (int) --> the number of times wait_random is executed
    max_delay (int) --> max delay for the coroutine

    Returns:
    List of all the delays in float values in ascending order
    """
    value = random.uniform(0, max_delay)
    await asyncio.sleep(value)
    return value
