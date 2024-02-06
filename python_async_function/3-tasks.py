#!/usr/bin/env python3
"""
this function just return Task type
"""
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    max_delay -> integer
    return: Task
    """
    return Task(wait_random(max_delay))
