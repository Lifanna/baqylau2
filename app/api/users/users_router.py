from fastapi import APIRouter
from . import users_api


api_router = APIRouter(
    prefix="/users",
)

api_router.include_router(
    users_api.router,
    tags=["users"]
)
