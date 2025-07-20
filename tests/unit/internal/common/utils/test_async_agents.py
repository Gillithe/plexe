"""Tests for asynchronous agent utilities."""

import time
import asyncio

from plexe.internal.common.utils import run_agents_concurrently


async def _slow(value: int) -> int:
    await asyncio.sleep(0.1)
    return value


def test_run_agents_concurrently_executes_tasks():
    start = time.perf_counter()
    results = run_agents_concurrently([lambda: _slow(1), lambda: _slow(2)])
    elapsed = time.perf_counter() - start
    assert results == [1, 2]
    assert elapsed < 0.2
