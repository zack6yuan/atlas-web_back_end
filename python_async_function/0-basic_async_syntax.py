#!/usr/bin/env python3
"""
Asynchronous coroutine that returns the random delay using the random module
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Parameters:
    max_delay (int) -> Max delay of the process

    Returns:
    The random delay from the function as a float
    If called with no argument, 10 is the default value
    """
    value = random.uniform(0, max_delay) # Random number between 0 and max_delay
    await asyncio.sleep(value) # assign the random delay to the execution
    return value # return the delay value
