#!/usr/bin/env python3
"""
this function return a function that multiple the argument
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    this function return a function that multiple the argument
    """

    def multiplierr(a: float) -> float:
        return a * multiplier

    return multiplierr
