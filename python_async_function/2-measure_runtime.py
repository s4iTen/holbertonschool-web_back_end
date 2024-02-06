#!/usr/bin/env python3
"""
this function return the average time per task
"""
import time
from typing import List
from asyncio import run, gather
from random import uniform
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    n -> integer
    max_delay -> integer
    return: float
    """
    start = time.time()
    await gather(wait_n(n, max_delay))
    end = time.time()
    total = end - start
    measure = total / n
    return measure
