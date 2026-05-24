from sqlmodel import SQLModel, Field
from typing import Optional


class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    hashed_password: str