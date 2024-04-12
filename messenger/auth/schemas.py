from pydantic import BaseModel
import uuid
import datetime


class UserPublic(BaseModel):
    """
    User public schema
    """
    id: uuid.UUID
    username: str


class User(BaseModel):
    """
    User schema
    """
    id: uuid.UUID
    username: str
    password: str
    created_at: datetime.datetime
    updated_at: datetime.datetime | None


class UserRegisterLoginRequestSchema(BaseModel):
    """
    User create and login request schema
    """
    username: str
    password: str


class UserCreateResponseSchema(BaseModel):
    """
    User create response schema
    """
    id: uuid.UUID
    username: str
    created_at: datetime.datetime


class UserLoginResponseSchema(BaseModel):
    """
    User login response schema
    """
    access_token: str



