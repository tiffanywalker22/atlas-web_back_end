#!/usr/bin/env python3
""" Returns sum of a list containing ints and floats """


def sum_mixed_list(mxd_lst: list) -> float:
    """
    Returns sum of a list containing ints and floats

    Args:
    - mxd_lst (list): The list containing integers and floats to be summed

    Returns:
    - float: The sum of the input list as a float
    """
    total = 0.0
    for num in mxd_lst:
        total += float(num)
    return total
