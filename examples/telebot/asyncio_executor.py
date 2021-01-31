import asyncio


async def non_blocking(loop, executor, *task):
    await asyncio.wait(
        fs={
            loop.run_in_executor(executor, task[0]),
            loop.run_in_executor(executor, task[1]),
        },
        return_when=asyncio.ALL_COMPLETED
    )