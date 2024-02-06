#!/usr/bin/env python3
"""
this function return a random delay between 0 and the max delay
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """
    max_delay -> variable of the max delay
    return: The delay number
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
