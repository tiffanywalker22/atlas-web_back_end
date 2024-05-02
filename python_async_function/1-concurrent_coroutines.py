#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""


import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n, max_delay):
    """
    Asynchronous routine that spawns n tasks of wait_random with
    the specified max_delay

    Args:
    - n (int): Number of tasks to spawn
    - max_delay (float): The maximum delay in seconds for each task

    Returns:
    - List[float]: List of all the delays (float values) in ascending order
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
