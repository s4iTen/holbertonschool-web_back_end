#!/usr/bin/env python3
"""
this function just yield random float between 0 and 10
"""
import random
import asyncio


async def async_generator():
    """
    there is no return or parameters

    float: A random float value between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield (random.uniform(0, 10))
