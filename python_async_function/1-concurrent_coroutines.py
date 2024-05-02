#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""

import asyncio
from random import random

async def wait_random(max_delay):
    """
    waits for a random amount of time up to max_delay

    Args:
    - max_delay (float): The maximum delay in seconds

    Returns:
    - float: The actual delay in seconds
    """
    delay = random() * max_delay
    await asyncio.sleep(delay)
    return delay

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
