#!/usr/bin/env python3
"""
this function Spawns wait_random n times with the specified max_delay
"""
import asyncio
from typing import List
from asyncio import gather
from random import uniform
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    n -> integer
    max_delay -> Maximum delay in seconds.

    Returns:list with type of float
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await gather(*tasks)
    delays = sorted(results)
    return delays
