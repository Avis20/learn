from enum import Enum, auto

from datetime import datetime, timedelta
from dataclasses import dataclass


class TariffPeriodUnit(str, Enum):
    day = auto()
    month = auto()
    year = auto()

@dataclass
class Tariff:
    name: str
    alias: str
    cost: str
    period: int
    period_unit: str


tariff = Tariff(
    name="base", 
    alias="base", 
    cost="5",
    period=1,
    period_unit=TariffPeriodUnit.month
)

print('\n\n')
print(tariff.period_unit)
print('\n\n')

to_days_map = {
    TariffPeriodUnit.day.value: 1,
    TariffPeriodUnit.month.value: 30,
    TariffPeriodUnit.year.value: 365,
}


period_start = datetime.utcnow()
period_end = datetime.utcnow() + timedelta(days=(to_days_map[tariff.period_unit]*tariff.period))

print('\n\n')
print(period_start)
print(period_end)
print('\n\n')

