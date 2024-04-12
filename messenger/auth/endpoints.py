from typing import Annotated

from fastapi import HTTPException, status, Depends
from fastapi.routing import APIRouter

from messenger.auth.schemas import User, UserRegisterLoginRequestSchema, UserLoginResponseSchema
from messenger.auth.table_data_gateways.user import UserTDG
from messenger.security import access_security

router = APIRouter()


@router.post("/register")
async def register(
        user: UserRegisterLoginRequestSchema
):
    """
    Register user
    """
    if registered := await UserTDG().register(user):
        return registered
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Something went wrong."
    )


@router.post("/login", response_model=UserLoginResponseSchema)
async def login(
        login_data: UserRegisterLoginRequestSchema
) -> UserLoginResponseSchema:
    """
    Login user
    """
    if not (user := await UserTDG().get_by_username(login_data.username)):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid credentials."
        )
    if user.password != login_data.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid credentials."
        )
    return UserLoginResponseSchema(
        access_token=access_security.create_access_token(subject=user.model_dump(mode="json", exclude={'password'}))
    )
