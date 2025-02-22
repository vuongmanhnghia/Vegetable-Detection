from fastapi import APIRouter, Request, Depends
from app.controllers import auth_controller
from app.middleware.require_authentication import require_authentication

authRouter = APIRouter()


@authRouter.post("/google")
async def google_login(token: str):
    return await auth_controller.google_login(token)


@authRouter.get("/me", dependencies=[Depends(require_authentication)])
async def me(request: Request):
    return await auth_controller.get_me(request)
