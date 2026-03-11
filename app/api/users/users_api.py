from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.users.users_schemas import UserRead
from data_access.db.session import get_db
from data_access.users.users_repository import UsersRepository
from business_logic.users.users_service import UsersService

router = APIRouter()

def get_users_service(db: AsyncSession = Depends(get_db)) -> UsersService:
    repo = UsersRepository(db)
    return UsersService(repo)

@router.get("/", response_model=list[UserRead])
async def get_users(
    service: UsersService = Depends(get_users_service)
):
    users = await service.get_users()

    return users

