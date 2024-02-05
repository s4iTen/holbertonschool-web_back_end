#!/usr/bin/env python3
import typing
"""
this function add each float in the list
"""


def sum_list(input_list: typing.List[float]) -> float:
    """
    input_list -> list with float elements inside
    temp -> the sum of the lists float
    return: the sum of the float inside the list
    """
    temp = 0
    for i in range(len(input_list)):
        temp += input_list[i]
    return float(temp)
