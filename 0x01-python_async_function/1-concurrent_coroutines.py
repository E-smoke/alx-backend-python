#!/usr/bin/env python3
'''
    The basics of async.
'''

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay:int) -> List[float]:
    """wait_n"""
    task_array = []
    delays = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        task_array.append(task)
    batch = asyncio.as_completed(task_array)
    for i in batch:
        delays.append(await i)
    return delays
