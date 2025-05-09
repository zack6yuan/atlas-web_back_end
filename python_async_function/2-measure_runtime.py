#!/usr/bin/env python3
"""
A measure time function that measures execution time
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_time(n: int, max_delay: int) -> float:
    """
    Parameters:
    n (integer) --> measures execution time
    max_delay (integer) --> max delay for the coroutine
    
    Methods:
    perf_counter() --> used for measuring durations
    and testing code performance

    Returns:
    total_time / n (float)
    """
    start = time.perf_counter() # Start time marker
    await (wait_n(n, max_delay)) # Await execution
    end = time.perf_counter() # End time marker

    total_time = end - start # Calculate total time

    return total_time / n # Return according to format
