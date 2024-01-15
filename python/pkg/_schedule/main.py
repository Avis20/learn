import asyncio
import calendar
from time import time
from croniter import croniter
from datetime import datetime


def to_unix(date):
    """Converts a datetime object to unixtime"""

    return calendar.timegm(date.utctimetuple())


def get_next_cron_timestamp(cron):
    itr = croniter(cron, datetime.utcnow())
    next_dt = itr.get_next(datetime)

    return next_dt


async def help():
    print(f"hello {datetime.now()}")
    await asyncio.sleep(1)


async def main():
    while True:
        cron_str = "0 0 * * 0"
        timestamp = to_unix(get_next_cron_timestamp(cron_str))
        while (sleep_time := timestamp - time()) > 0:
            print(sleep_time)
            await asyncio.sleep(sleep_time)
        await help()


if __name__ == "__main__":
    asyncio.run(main())
