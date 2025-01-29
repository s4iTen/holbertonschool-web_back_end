#!/usr/bin/env python3

def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters."""
    if page <= 1:
        return (0, page_size)

    Start_index = ((page - 1) * page_size)
    End_index = (page * page_size)

    return (Start_index, End_index)
