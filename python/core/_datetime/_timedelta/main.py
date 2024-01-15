
from datetime import datetime, timedelta
from dataclasses import dataclass

from dateutil.relativedelta import relativedelta

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
    period_unit='month'
)

print('\n\n')
print(tariff.period_unit)
print('\n\n')

period_unit_map = {
    'month': 'months'
    'year': 'months'
}
per2 = {per[tariff.period_unit]: tariff.period}

period_start = datetime.utcnow()
period_end = datetime.utcnow() + relativedelta(**per2)

print('\n\n')
print(period_start)
print(period_end)
print('\n\n')

