from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        for period in self.dates:
            date_start, date_end = period
            periods = []
            while date_start <= date_end:
                periods.append(date_start)
                date_start += timedelta(days=1)
            yield from periods



m = Movie('sw', [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

for d in m.schedule():
    print(d)