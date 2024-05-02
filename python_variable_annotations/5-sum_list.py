#!/usr/bin/env python3
""" Return the sum of list of floats """


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
    - input_list (List[float]): The list of float numbers to be summed.

    Returns:
    - float: The sum of the input list as a float.
    """
    return sum(input_list)
