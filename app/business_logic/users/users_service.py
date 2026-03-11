from data_access.users.users_repository import UsersRepository
from data_access.db.models.user import User
from api.users.users_schemas import UserRead

class UsersService:
    def __init__(self, repo: UsersRepository):
        self.repo = repo
    
    async def get_users(self):
        return await self.repo.get_all()
