import enum


class TimelineProgramPath(str, enum.Enum):
    path = "/api/v1/programs/{id}"
    method = "GET"
