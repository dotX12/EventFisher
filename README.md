# EventFisher
#### This project is a draft, on the basis of which you can create an asynchronous handler for your API requests and call functions if any handler is triggered.
The project is based on a aiohttp, asyncio, custom async scheduler and AsyncEventEmitter.

Every 30 seconds, the scheduler calls def poll from BlockcypherAPI, poll in turn calls a number of other functions. These functions make emit, which our decorators run.

#### Where applicable:

I have implemented a simple but high-quality example.
Every 30 seconds we check whether new transactions have come to our wallet, as well as whether the network commission has changed.
If any of this is fulfilled, an "emit" will be made, which will trigger decorators and call our functions, which in turn will do something. In these functions, you can log, add to the database, send message to users, etc.

```python
    async def get_info_medium_fee(self):
        resp = await self.request('GET', MAIN_INFO_BTC)
        if self.medium_fee != resp['medium_fee_per_kb']:
            self.medium_fee = resp['medium_fee_per_kb']
            self.emit('new_btc_medium_fee')
            # Will call the event handler that belongs to this decorator 
            # @event.on('new_btc_medium_fee')
```
```python
@event.on('new_btc_medium_fee')
def btc_new_price():
    print(f'BTC NEW MEDIUM FEE: {event.medium_fee}')

```
