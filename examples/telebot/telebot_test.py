import asyncio
from scheduler.scheduler import Scheduler
import concurrent.futures
from examples.telebot import non_blocking, event, bot

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.ensure_future(event.create_session()))
scheduler = Scheduler([event], loop)
executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)
loop.run_until_complete(non_blocking(loop, executor, bot.polling, scheduler.run_forever))
