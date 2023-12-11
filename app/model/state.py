from sqlmodel import Field, SQLModel
from typing import Optional

class StateBase(SQLModel):
    id: Optional[int]
    name: str
    secret_name: str
    age: Optional[int] = None


class State(StateBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)