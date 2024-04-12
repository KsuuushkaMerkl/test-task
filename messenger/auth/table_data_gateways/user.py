from edgedb import AsyncIOClient

from database import edgedb_client
from messenger.auth.schemas import User, UserRegisterLoginRequestSchema


class UserTDG:
    """
    User TDG
    """

    def __init__(self):
        self.database: AsyncIOClient = edgedb_client

    async def get_by_username(self, username: str) -> User | None:
        """
        Get user by username
        """
        query = """
        select User { * } filter .username = <str>$username
        """
        user = await self.database.query_single_json(query, username=username)
        return User.model_validate_json(user) if user else None

    async def register(self, user: UserRegisterLoginRequestSchema):
        """
        Register user
        """
        query = """
        insert User {
            username := <str>$username,
            password := <str>$password 
        }
        """
        return await self.database.query(query, **user.model_dump())
