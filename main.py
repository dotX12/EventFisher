import asyncio
from API.blockcypher import *
from scheduler.scheduler import Scheduler

event = BlockcypherAPI()


@event.on('new_transaction')
def new_transaction():
    print('New Transaction!'
          f'TX Hash: {event.tx["tx_hash"]}')


@event.on('new_btc_medium_fee')
def btc_new_price():
    print(f'BTC NEW MEDIUM FEE: {event.medium_fee}')


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.ensure_future(event.create_session()))
sch = Scheduler([event])
sch.run_forever()

