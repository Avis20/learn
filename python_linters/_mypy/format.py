
from dataclasses import dataclass
from dto import TimelineProgramPath


@dataclass
class Programs:
    id: int


def test(q: str):
    return "".join([TimelineProgramPath.path, f"/{q}"])


# p = Programs(12)
print(test("12"))
