import asyncio
from pyee import AsyncIOEventEmitter


class Scheduler(AsyncIOEventEmitter):
    def __init__(self, modules: list, loop, poll_delay: int = 2):
        """
        :param modules: modules to poll
        :param poll_delay: how long to wait after polling finishes until polling starts again
        """
        self.modules = modules
        self.poll_delay = poll_delay
        self.loop = loop
        AsyncIOEventEmitter.__init__(self, loop=loop)

    async def _run_forever(self):
        while True:
            self.emit('global_start_poll')
            for foo in self.modules:
                await foo.poll()
            self.emit('global_end_poll')
            await asyncio.sleep(self.poll_delay)

    def run_forever(self):
        self.loop.create_task(self._run_forever())
        self.loop.run_forever()
