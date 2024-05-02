#!/usr/bin/env python3
""" four parallel comprehensions """

import asyncio
from typing import List
import time


async_comprehension = __import__('1-async_comprehension.py').async_comprehension


async def measure_runtime() -> float:
    """Import async_comprehension from the previous file and write a
    measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.
    measure_runtime should measure the total runtime and return it."""
    start: float = time.time()
    runner = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*runner)
    return (time.time() - start)
