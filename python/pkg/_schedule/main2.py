import time
import asyncio
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from croniter import croniter


def tick():
    print("Tick! The time is: %s" % datetime.now())


async def main():
    scheduler = AsyncIOScheduler()
    cron_str = '* * * * *'
    scheduler.add_job(tick, 'cron', minute='*')
    scheduler.start()
    while True:
        await asyncio.sleep(1000)


if __name__ == "__main__":
    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
