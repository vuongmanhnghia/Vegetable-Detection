from fastapi import APIRouter, Request, Depends
from app.controllers import auth_controller


authRouter = APIRouter()


@authRouter.post("/google")
async def google_login(token: str):
    return await auth_controller.google_login(token)


@authRouter.get("/me")
async def me(user_id: str):
    return await auth_controller.get_me(user_id)
