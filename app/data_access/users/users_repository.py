from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from api.users.users_schemas import UserRead
from data_access.db.models import User


class UsersRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> list[UserRead]:
        result = await self.db.execute(
            select(
                User.id,
                User.first_name,
                User.last_name,
                User.email,
                User.phone
            )
        )

        rows = result.all()

        return [
            UserRead(
                id=row.id,
                first_name=row.first_name,
                last_name=row.last_name,
                email=row.email,
                phone=row.phone
            )
            for row in rows
        ]
