#!/usr/bin/env python3
"""
Coroutine that loops 10 times, and yields a random number between 0 and 10
"""
import asyncio
import random
from typing import Generator

"""
Generator Format:
    - YieldType --> Value that the generator will yield
    - SendType --> Value type that is sent to the generator
    - ReturnType --> Value type that the generator will return
"""


async def async_generator() -> Generator[float, None, None]:
    """
    Parameters:
    - None

    Method:
    - Iterate from 0 to 10
    - Asynchronously wait 1 second
    - Yield random number

    Returns:
    - Random number (float) between 0 and 10
    ""
    for x in range(0, 10):
        await asyncio.sleep(1)
        yield (random.uniform(0, 10))
    """
