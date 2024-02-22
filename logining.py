from aiofile import async_open
from datetime import datetime


async def logining(text):
    async with async_open('../logs.txt', 'a') as f:
        await f.write(f'{text}\n')
        await f.write(f'Time: {datetime.now()}\n')
        await f.write('\n')