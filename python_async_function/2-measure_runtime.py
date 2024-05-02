#!/usr/bin/env python3
"""Measure the runtime"""


import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(max_delay: int = 10, n: int = 0) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per task

    Args:
    - n (int): Number of tasks to spawn in wait_n
    - max_delay (int): Maximum delay in seconds for each task in wait_n

    Returns:
    - float: Average time per task in seconds
    """
    first_time = time.perf_counter()
    asyncio.run(wait_n(max_delay, n))
    elapsed = time.perf_counter() - first_time
    total_time = elapsed / n

    return total_time
