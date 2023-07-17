from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    test: int

data = {
    "id": 1,
    "name": "user"
}

test_response = User.parse_obj(data)
