from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from sqlalchemy import func
from datetime import datetime
import uuid

class User(SQLModel, table = True):
    __tablename__ = "users"
    
    uid: uuid.UUID = Field(sa_column = Column(pg.UUID,default=uuid.uuid4, primary_key=True, nullable=False))
    username: str = Field(index=True, unique=True, nullable=False)
    email: str = Field(index=True, unique=True, nullable=False)
    password_hash: str = Field(
        sa_column=Column(pg.VARCHAR, nullable=False), exclude=True
    )
    first_name: str =Field(nullable=True)
    last_name: str= Field(nullable=True)
    is_verified: bool= Field(default=False, nullable=False)
    created_at: datetime= Field(sa_column=Column(pg.TIMESTAMP(timezone=True), server_default=func.now()))
    updated_at: datetime =Field(sa_column=Column(pg.TIMESTAMP(timezone=True), onupdate=func.now(), nullable=True))
    
    def __repr__(self):
        return f"<User {self.username}>"