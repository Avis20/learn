

import asyncio
import random


async def func():
    rand = random.random()
    await asyncio.sleep(rand)
    return rand


async def value():
    result = await func()
    print(result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(value())
    loop.close()

