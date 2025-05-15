#!/usr/bin/env python3
"""
Function that returns an asyncio.Task
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_n(max_delay: int) -> asyncio.Task:
    """
    Parameters:
    max_delay (integer) --> integer accepted as input

    Methods:
    call task_wait_random

    Returns:
    asyncio.Task (float) --> used to manage coroutines
    """
    task_wait_random() 
