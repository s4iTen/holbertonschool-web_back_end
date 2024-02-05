#!/usr/bin/env python3
"""
return the sum of the float and the integers inside the list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    mxt_lst -> list with mixed elements(float and integers)
    return: the sum of the elements inside the list
    """
    return sum(mxd_lst)
