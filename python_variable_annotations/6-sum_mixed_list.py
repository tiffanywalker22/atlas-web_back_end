#!/usr/bin/env python3
""" Returns sum of a list containing ints and floats """

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Returns sum of a list containing ints and floats

    Args:
    - mxd_list: The list containing integers and floats to be summed

    Returns:
    - float: The sum of the input list as a float
    """
    return sum(mxd_list)
