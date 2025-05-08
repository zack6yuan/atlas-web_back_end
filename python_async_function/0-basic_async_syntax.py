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
    The random delay from the function
    """
    for i in range(0, max_delay):