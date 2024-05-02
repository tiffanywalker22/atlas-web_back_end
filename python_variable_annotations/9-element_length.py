#!/usr/bin/env python3
""" Returns a list of tuples containing elements and their lengths """


from typing import Iterable, Sequence, List, Union, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing elements and their lengths

    Args:
    - lst: The list of strings

    Returns:
    A list of tuples where each tuple contains an element from lst and its length
    """
    return [(i, len(i)) for i in lst]
