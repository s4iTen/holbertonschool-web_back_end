#!/usr/bin/env python3
"""
this function return a tuple that contain string and float
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    this is the return of tuple
    """
    return (k, v**2)
