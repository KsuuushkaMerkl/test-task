from pydantic import BaseModel
import uuid
import datetime

from messenger.auth.schemas import UserPublic


class Post(BaseModel):
    """
    Post schema
    """
    id: uuid.UUID
    user: UserPublic
    text: str


class PostCreateRequestSchema(BaseModel):
    """
    Create post request schema
    """
    text: str


class PostCreateResponseSchema(BaseModel):
    """
    Create post response schema
    """
    id: uuid.UUID
    text: str
    created_at: datetime.datetime


class PostUpdateRequestSchema(BaseModel):
    """
    Post update request schema
    """
    text: str


class PostUpdateResponseSchema(BaseModel):
    """
    Post update response schema
    """
    id: uuid.UUID
    text: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class PostDeleteResponseSchema(BaseModel):
    """
    Delete request schema
    """
    id: uuid.UUID

