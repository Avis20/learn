from collections import defaultdict


test = [1, 2, 3]
print('\n\n')
print(test[-1])
print(1 in test)
print('\n\n')




from uuid import uuid4
from enum import Enum
from uuid import UUID
from typing import ClassVar

from pydantic import BaseModel, BaseConfig, Field

class PlayerMonitoringStatus(Enum):
    unknown = ""
    pause = "1"
    playing = "2"

    @classmethod
    def _missing_(cls, values):
        return cls.unknown


class PlayerMonitoringDomain(BaseModel):
    play_status: PlayerMonitoringStatus
    request_time_diff: int
    track_id: UUID
    filial_key: UUID
    artist: str
    track_name: str
    playlist_name: str
    playlist_id: str

    MAX_REQUEST_TIME_DIFF: ClassVar[int] = 3 * 60  # 3 мин.

    _MAP_FROM_MONITORING: ClassVar[dict] = {
        "current_track_id": "track_id"
    }

    @classmethod
    def convert_to_domain(cls, **kwargs):
        for key, value in cls._MAP_FROM_MONITORING.items():
            if key in kwargs:
                kwargs[value] = kwargs[key]
        return PlayerMonitoringDomain.parse_obj(kwargs)

""" v2
    class Config(BaseConfig):
        fields = {
            "track_id": "current_track_id"
        }

        @classmethod
        def get_field_info(cls, name):
            print(name)
            field_config = super().get_field_info(name) or {}
            print(field_config)
            return field_config
"""


""" v1 
    _MAP_FROM_MONITORING: ClassVar[dict] = {
        "current_track_id": "track_id"
    }

    def __init__(self, **kwargs):
        for key, value in self._MAP_FROM_MONITORING.items():
            if key in kwargs:
                kwargs[value] = kwargs[key]
        super().__init__(**kwargs)
"""


if __name__ == '__main__':
    
    monitoring = {
        "play_status": 2,
        "key": 1,
        "request_time_diff": 13,
        "key": UUID("56bd034d-0000-0019-0000-0000aaa00e6b"),
        "current_track_id": "56bd034d-0000-0019-0000-0000aaa00e6b",
    }

    play_status = monitoring.get("play_status", "")

    player_monitoring = PlayerMonitoringDomain(**monitoring)

    monitoring = {
        "play_status": 2,
        "request_time_diff": 10,
        "filial_key": UUID("56bd034d-0000-0019-0000-0000aaa00e6b"),
        "current_track_id": UUID("56bd034d-0000-0019-0000-0000aaa00e6b"),
        # "track_id": UUID("56bd034d-0000-0019-0000-0000aaa00e6b"),
        "artist": "",
        "track_name": "",
        "playlist_name": "",
        "playlist_id": "",
    }
    player_monitoring = PlayerMonitoringDomain.convert_to_domain(**monitoring)
    print(player_monitoring.track_id)

    # print('\n\n')
    # print(player_monitoring)
    # print('\n\n')
