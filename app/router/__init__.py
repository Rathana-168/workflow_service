from fastapi import APIRouter
from .state import router as state
from .transition import router as transition


api_v1 = APIRouter()

api_v1.include_router(state, tags=["state"])
api_v1.include_router(transition, tags=["trans"])
