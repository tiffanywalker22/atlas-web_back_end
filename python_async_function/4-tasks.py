#!/usr/bin/env python3
"""Tasks"""


import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    """
    spawns n tasks of task_wait_random with the specified max_delay

    Args:
    - n (int): Number of tasks to spawn
    - max_delay (float): The maximum delay in seconds for each task

    Returns:
    - List[float]: List of all the delays (float values) in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)

