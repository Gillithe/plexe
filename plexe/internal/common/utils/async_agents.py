"""Utility helpers for running agent tasks concurrently."""

from typing import Awaitable, Callable, Iterable, List, Any
import asyncio


def run_agents_concurrently(agents: Iterable[Callable[[], Awaitable[Any]]]) -> List[Any]:
    """Run multiple asynchronous agent tasks concurrently.

    Args:
        agents: Iterable of callables returning awaitable tasks.

    Returns:
        List of agent results in the order they were supplied.
    """

    async def _run() -> List[Any]:
        tasks = [asyncio.create_task(agent()) for agent in agents]
        return await asyncio.gather(*tasks, return_exceptions=True)

    return asyncio.run(_run())
