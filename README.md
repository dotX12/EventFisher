# EventFisher
#### This project is a draft, on the basis of which you can create an asynchronous handler for your API requests and call functions if any handler is triggered.
The project is based on a aiohttp, asyncio, custom async scheduler and AsyncEventEmitter.

Every 30 seconds, the scheduler calls def poll from BlockcypherAPI, poll in turn calls a number of other functions. These functions make emit, which our decorators run.

#### ***How to start?***
```
💲 git clone https://github.com/dotX12/EventFisher/
💲 cd EventFisher
💲 pip3 install -r requirements.txt
💲 python3 main.py
```
#### Where applicable:

I have implemented a simple but high-quality example.
Every 30 seconds we check whether new transactions have come to our wallet, as well as whether the network commission has changed.
If any of this is fulfilled, an "emit" will be made, which will trigger decorators and call our functions, which in turn will do something. In these functions, you can log, add to the database, send message to users, etc.

```python3
    async def get_info_medium_fee(self):
        resp = await self.request('GET', MAIN_INFO_BTC)
        if self.medium_fee != resp['medium_fee_per_kb']:
            self.medium_fee = resp['medium_fee_per_kb']
            self.emit('new_btc_medium_fee')
            # Will call the event handler that belongs to this decorator 
            # @event.on('new_btc_medium_fee')
```
```python3
@event.on('new_btc_medium_fee')
def btc_new_price():
    print(f'BTC NEW MEDIUM FEE: {event.medium_fee}')

```


An example was also added for the telebot library, which sends information to the user when the decorator is triggered.
```python3
@event.on('new_transaction')
def new_transaction():
    bot.send_message(ADMIN_ID, f'New Transaction! TX Hash: {event.tx["tx_hash"]}')


@event.on('new_btc_medium_fee')
def btc_new_price():
    bot.send_message(ADMIN_ID, f'BTC NEW MEDIUM FEE: {event.medium_fee}')
```
