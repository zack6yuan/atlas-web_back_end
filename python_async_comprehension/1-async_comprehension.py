#!/usr/bin/env python3
"""
Coroutine that collects 10 random numbers, then returns the numbers
"""
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> float:
    for x in range(async_generator):
        
