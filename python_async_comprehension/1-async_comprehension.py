#!/usr/bin/env python3
"""
this coroutine collect 10 num and return them
"""
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    this coroutine collect 10 num and return them
    """
    return [i async for i in async_generator()]
