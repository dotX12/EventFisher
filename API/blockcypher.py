import time

import aiohttp
from pyee import EventEmitter
from options import *


class BlockcypherAPI(EventEmitter):
    def __init__(self, poll_delay: int = 30):
        EventEmitter.__init__(self)
        self.poll_delay = poll_delay
        self.last_poll = 0
        self.tx = {}
        self.medium_fee = 0
        self.session = ...

    async def create_session(self):
        self.session = aiohttp.ClientSession()

    async def request(self, method: str, url: str, **data: str):

        if method.lower() == 'get':
            async with self.session.get(url, params=data) as resp:
                j = await resp.json()
                return j
        elif method.lower() == 'post':
            async with self.session.post(url, data=data) as resp:
                j = await resp.json()
                return j
        elif method.lower() == 'delete':
            async with self.session.delete(url, data=data) as resp:
                j = await resp.json()
                return j
        elif method.lower() == 'put':
            async with self.session.put(url, data=data) as resp:
                j = await resp.json()
                return j
        else:
            raise ValueError(f"Invalid method: {method}")

    async def check_new_transaction(self):
        resp = await self.request('GET', f"{URL_CHECK_TRANSACTIONS.format(address)}?limit=5")
        if resp["txrefs"][0] != self.tx:
            self.tx = resp["txrefs"][0]
            self.emit("new_transaction")

    async def get_info_medium_fee(self):
        resp = await self.request('GET', MAIN_INFO_BTC)
        if self.medium_fee != resp['medium_fee_per_kb']:
            self.medium_fee = resp['medium_fee_per_kb']
            self.emit('new_btc_medium_fee')

    async def poll(self):
        if time.time() - self.last_poll > self.poll_delay:
            self.emit("start_poll")
            await self.check_new_transaction()
            await self.get_info_medium_fee()
            self.emit("end_poll")
            self.last_poll = time.time()
