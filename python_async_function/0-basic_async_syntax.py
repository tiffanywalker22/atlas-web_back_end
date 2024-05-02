#!/usr/bin/env python3
"""Syntax wait"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds

    Parameters:
    - max_delay (int): Maximum delay in seconds

    Returns:
    - float: Random delay in seconds
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
