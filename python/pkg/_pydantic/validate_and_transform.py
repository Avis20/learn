import enum
import dataclasses

from typing import Optional, List
from datetime import date, datetime, timedelta, time
from pydantic import BaseModel, Field, validator, root_validator
from datetime import date

class RenderType(str, enum.Enum):
    """Справочник визуализации сетки вещания: по программам или сегментам"""
    programs = "PROGRAMS"
    segments = "SEGMENTS"

class StreamType(str, enum.Enum):
    """справочник типов (type)"""
    RADIO = "RADIO"
    TV = "TV"
    INTERNET = "INTERNET"

@dataclasses.dataclass
class BaseDto:
    def as_dict(self):
        return dataclasses.asdict(self)

@dataclasses.dataclass
class ProgramDto(BaseDto):
    id: int


@dataclasses.dataclass
class SegmentDto(BaseDto):
    id: str


@dataclasses.dataclass
class BroadcastDto(BaseDto):
    render: RenderType
    channel_type: StreamType
    search: Optional[str] = None
    channel_id: Optional[List[int]] = None
    period_from: Optional[date] = None
    period_to: Optional[date] = None


class BroadcastRequest(BaseModel):
    search: Optional[str] = Field(None, title="Строка поиска", description="""Поиск осуществляется по:
            - расшифрованному тексту из аудио
            - обнаруженному тексту из видео
    """)
    render: Optional[str] = Field(None)
    period_from: Optional[date] = Field(
        None,
        alias='period-from'
    )
    channel_id: Optional[list[int]] = Field(
        None,
        alias='channel_id[]'
    )
    # channel_type: Optional[str] = Field(None, alias="channel-type")
    # period_to: Optional[date] = Field(None, alias="period-to", description="""Получаем список
    #     programs или segments у которых time_end <= выбранной дате
    # """)

    # @validator('period_from')
    # def valid(cls, value):
    #     period_from = datetime.combine(value, time(0, 0))
    #     return int(period_from.timestamp())


    @validator('channel_id')
    def _channel_id(cls, value: List[int]) -> List[int]:
        print(value)
        return value


    class Config:
        allow_population_by_field_name = True
        allow_population_by_alias = True


if __name__ == '__main__':
    channels = list([17, 1])

    broadcast = BroadcastDto(
        render=RenderType.programs,
        channel_type=StreamType.TV,
        channel_id=channels,
        period_from=datetime.utcnow() - timedelta(minutes=10),
        period_to=datetime.utcnow()
    )
    request = BroadcastRequest(
        search=broadcast.search,
        render=broadcast.render.value,
        period_from=broadcast.period_from,
        # period_to=broadcast.period_to,
        channel_id=broadcast.channel_id,
        # channel_type=broadcast.channel_type,
    )
    print('\n\n')
    print(request.dict())
    print(request.dict(by_alias=True))
    print('\n\n')


