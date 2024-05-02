#!/usr/bin/env python3
"""Tasks"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task for the wait_random function with a specified maximum delay

    Args:
    - max_delay (int): The maximum delay in seconds for wait_random

    Returns:
    - asyncio.Task: An asyncio Task representing the execution of wait_random(max_delay)
    """
    return asyncio.create_task(wait_random(max_delay))
