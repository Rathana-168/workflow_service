from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from typing import List

from app.model.state import StateBase, State

from app.database import get_async_db

router = APIRouter(prefix="/state")

@router.get("/")
async def get_one(db: AsyncSession = Depends(get_async_db)):
    statement = select(State)
    result = await db.execute(statement)
    return result.scalars().all()

@router.get("/list")
async def get_list(db: AsyncSession = Depends(get_async_db)):
    statement = select(State)
    result = await db.execute(statement)
    return result.scalars().all()