#!/usr/bin/env python3
""""""
import time
import typing
from asyncio import gather
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start = time.time()
    await gather(async_comprehension(),
                 async_comprehension(),
                 async_comprehension(),
                 async_comprehension())

    end = time.time()
    return end - start
    