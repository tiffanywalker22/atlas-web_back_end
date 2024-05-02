#!/usr/bin/env python3
"""  Returns tuple with string k and the square of int/float v """


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns tuple with the string k and the square of int/float v

    Args:
    - k (str): The string key
    - v (Union[int, float]): The integer or float value

    Returns:
    - tuple: A tuple containing k and the square of v as a float
    """
    return (k, float(v) ** 2)
