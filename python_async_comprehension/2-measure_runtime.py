#!/usr/bin/env python3
"""
Coroutine that executes async_comprehension
4 times in parallel using asyncio.gather
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension.py').async_comprehension


async def measure_runtime() -> float:
    process1 = async_comprehension()
    process2 = async_comprehension()
    process3 = async_comprehension()
    process4 = async_comprehension()

    process_results = await asyncio.gather(process1, process2, process3, process4)

    return process_results
