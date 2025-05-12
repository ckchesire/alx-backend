#!/usr/bin/env python3
"""Module that returns the range of indexes corresponding to a list for
particular pagination parameters
"""


def index_range(page: int, page_size: int) -> tuple:
    """Function to return a tuple containing a start index and an end index.

       Args:
          page(int) - Start page number
          page_size(int) - Page size number

       Returns:
          A tuple with start and end pages
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
