from sqlmodel import Field, SQLModel
from typing import Optional


class RequestBase(SQLModel):
    id: Optional[int]
    name: str


class Request(RequestBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
