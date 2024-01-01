from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional


class StateBase(SQLModel):
    id: Optional[int]
    name: str


class State(StateBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class ActionBase(SQLModel):
    id: Optional[int]
    name: str


class Action(ActionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class TransitionBase(SQLModel):
    id: Optional[int]
    name: str
    source_id: Optional[int]
    dest_id: Optional[int]
    action_id: Optional[int]
    workflow_id: Optional[int]
    conditions: Optional[str]
    prepare: Optional[str]
    after: Optional[str]
    before: Optional[str]


class Transition(TransitionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    source_id: Optional[int] = Field(default=None, foreign_key="state.id")
    dest_id: Optional[int] = Field(default=None, foreign_key="state.id")
    action_id: Optional[int] = Field(default=None, foreign_key="action.id")
    workflow_id: Optional[int] = Field(default=None, foreign_key="workflow.id")
    # workflow: Optional["WorkflowBase"] = Relationship(back_populates="transitions")


class WorkflowBase(SQLModel):
    id: Optional[int]
    name: str
    description: str
    # transitions: List["TransitionBase"]


class Workflow(WorkflowBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # transitions: List["Transition"] = Relationship(back_populates="workflow")