from fastapi import APIRouter  # type: ignore

router = APIRouter()

# from .user_router import userRouter
from .auth_router import authRouter
from .user_router import userRouter


@router.get("/")
async def index():
    return {"message": "Hello FastAPI"}


router.include_router(userRouter, prefix="/users", tags=["users"])
router.include_router(authRouter, prefix="/auth", tags=["auth"])
