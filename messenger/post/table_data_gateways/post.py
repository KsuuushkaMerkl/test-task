import uuid

import edgedb.errors
from edgedb import AsyncIOClient

from database import edgedb_client
from messenger.post.schemas import Post


class PostTDG:
    """
    Post TDG
    """

    def __init__(self):
        self.database: AsyncIOClient = edgedb_client

    async def get_all(self) -> list[Post]:
        """
        Get all posts
        """
        query = """
        select Post { *, user: {id,username} }
        """
        return await self.database.query(query)

    async def get_by_user_id(self, user_id: uuid.UUID) -> list[Post]:
        """
        Get posts by user id
        """
        query = """
        select Post { *, user: {id, username} } filter .user.id = <uuid>$user_id
        """
        return await self.database.query(query, user_id=user_id)

    async def create_post(self, user_id: uuid.UUID, text: str):
        """
        Create new post
        """
        query = """
        insert Post {
            user := (select detached User {*} filter .id = <uuid>$user_id),
            text := <str>$text
        }
        """
        return await self.database.query(query, user_id=user_id, text=text)

    async def update_post(self,
                          post_id: uuid.UUID,
                          text: str | None = None) -> Post | None:
        """
        Update post
        """
        query = """
        with 
            text := <optional str>$text
        select (update Post filter .id = <uuid>$post_id set {text := text ?? .text}) { *, user: {id,username} }
        """

        try:
            return (await self.database.query(query, post_id=post_id, text=text))[0]
        except edgedb.errors.EdgeDBError as e:
            print(e)
            return None

    async def delete_post(self, post_id: uuid.UUID, user_id: uuid.UUID) -> uuid.UUID | None:
        """
        Delete post
        """
        query = """
        delete Post 
        filter
         (.id = <uuid>$post_id) 
        and
         (.user.id = <uuid>$user_id)
        """
        try:
            return await self.database.query_single(query, post_id=post_id, user_id=user_id)
        except edgedb.errors.EdgeDBError as e:
            print(e)
            return None
