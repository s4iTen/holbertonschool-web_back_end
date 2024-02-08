#!/usr/bin/env python3
"""
this coroutine measure the time of the execution of the previous coroutine four time"""
import time
from asyncio import gather
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    this coroutine measure the time of the execution of the previous coroutine four time
    """
    start = time.time()
    await gather(async_comprehension(),
                 async_comprehension(),
                 async_comprehension(),
                 async_comprehension())

    end = time.time()
    return end - start
