import asyncio
from blockcypher import *
from scheduler import Scheduler

event = BlockcypherAPI()


@event.on('new_transaction')
def new_transaction():
    print('New Transaction!'
          f'TX Hash: {event.tx["tx_hash"]}')


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.ensure_future(event.create_session()))
sch = Scheduler([event])
sch.run_forever()

