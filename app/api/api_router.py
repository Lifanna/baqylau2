from fastapi import APIRouter
from api.users.users_router import api_router as users_router

api_router = APIRouter()

api_router.include_router(
    users_router,
    prefix="/api"
)
