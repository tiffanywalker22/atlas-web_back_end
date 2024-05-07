#!/usr/bin/env python3
"""Write a function named index_range that takes
two integer arguments page and page_size"""


def index_range(page, page_size):
    """
    Args:
    - page (int): The 1-indexed page number
    - page_size (int): The size of each page

    Returns:
    - tuple: A tuple containing the start index and end index
    for the specified page in the paginated list
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
