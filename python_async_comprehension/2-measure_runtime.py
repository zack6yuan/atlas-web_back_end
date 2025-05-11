#!/usr/bin/env python3
"""
Coroutine that executes async_comprehension
4 times in parallel using asyncio.gather
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Parameters: None

    Methods:
    While async_comprehension is executed, start a time counter and log
    asyncio.gather --> execute multiple coroutines, and wait for them to complete

    Returns:
    Total time for the execution of the coroutine
    """
    start = time.perf_counter()  # Start time marker

    process1 = async_comprehension()
    process2 = async_comprehension()
    process3 = async_comprehension()
    process4 = async_comprehension()

    await asyncio.gather(process1, process2, process3, process4)

    end = time.perf_counter()  # End time marker

    process_results = end - start  # Total time calculation

    return process_results
