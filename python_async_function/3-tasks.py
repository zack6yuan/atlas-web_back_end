#!/usr/bin/env python3
"""
Function that returns an asyncio.Task
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Parameters:
    max_delay (integer) --> integer accepted as input

    Returns:
    asyncio.Task --> used to manage coroutines
    a float value is retuned
    """
    return asyncio.Task