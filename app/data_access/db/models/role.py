from sqlalchemy import (Column, String, TIMESTAMP)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.sql import func
from data_access.db.base import Base


class Role(Base):
    __tablename__ = 'roles'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    name = Column(String(50), nullable=False, unique=True)

    created_at = Column(TIMESTAMP, server_default=func.now())

    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    users = relationship("User", back_populates="role")
