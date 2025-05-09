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

    Methods:
    asyncio.create_task --> creates an asyncio.Task object

    Returns:
    asyncio.Task (float) --> used to manage coroutines
    """
    new_task = asyncio.create_task(wait_random(max_delay))
    return new_task
