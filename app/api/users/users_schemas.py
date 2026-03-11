from pydantic import BaseModel, EmailStr
from uuid import UUID


class UserRead(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: EmailStr
    phone: str | None

    class Config:
        from_attributes = True
