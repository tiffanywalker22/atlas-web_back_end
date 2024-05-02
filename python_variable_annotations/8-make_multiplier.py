#!/usr/bin/env python3
"""Returns a function that multiplies a float by a given multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a given multiplier

    Args:
    - multiplier (float): The multiplier to be used by the returned function

    Returns:
    - callable: A function that multiplies a float by the multiplier
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
