from fastapi import FastAPI

from messenger.auth.endpoints import router as auth_router
from messenger.post.endpoints import router as post_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(post_router, prefix="/post")
