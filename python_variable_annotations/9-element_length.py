#!/usr/bin/env python3
"""
this function return the elements length
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    lst -> this is the element
    return: return the elements length
    """
    return [(i, len(i)) for i in lst]
