import uuid
from typing import Annotated

from fastapi import HTTPException, status, Security, Depends
from fastapi.routing import APIRouter
from fastapi_jwt import JwtAuthorizationCredentials

from messenger.post.schemas import Post, PostCreateRequestSchema, PostUpdateRequestSchema, PostDeleteResponseSchema
from messenger.post.table_data_gateways.post import PostTDG
from messenger.security import access_security

router = APIRouter()


@router.get("/", response_model=list[Post])
async def get_all_posts() -> list[Post]:
    """
    Get all posts
    """
    return await PostTDG().get_all()


@router.get("/{user_id}", response_model=list[Post])
async def get_posts_by_user_id(
        user_id: uuid.UUID
) -> list[Post]:
    """
    Get posts by id
    """
    return await PostTDG().get_by_user_id(user_id)


@router.post("/", response_model=Post)
async def create_post(
        post: Annotated[PostCreateRequestSchema, Depends()],
        user: JwtAuthorizationCredentials = Security(access_security)
) -> Post:
    """
    Create new post
    """
    if created_post := await PostTDG().create_post(user["id"], post.text):
        return created_post
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Something went wrong."
    )


@router.patch("/{post_id}", response_model=Post)
async def update_post(
        post_id: uuid.UUID,
        post: Annotated[PostUpdateRequestSchema, Depends()],
        user: JwtAuthorizationCredentials = Security(access_security)  # noqa
) -> Post:
    """
    Update post
    """
    if updated_post := await PostTDG().update_post(post_id, post.text):
        return updated_post
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Something went wrong."
    )


@router.delete("/{post_id}", response_model=PostDeleteResponseSchema)
async def delete_post(
        post_id: uuid.UUID,
        user: JwtAuthorizationCredentials = Security(access_security)  # noqa
) -> PostDeleteResponseSchema:
    """
    Delete post
    """
    if await PostTDG().delete_post(post_id, user["id"]):
        return PostDeleteResponseSchema(id=post_id)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Post not found."
    )




