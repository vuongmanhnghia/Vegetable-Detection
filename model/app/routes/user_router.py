from fastapi import APIRouter, File, UploadFile
from app.controllers import user_controller
from app.middleware.require_authentication import require_authentication

userRouter = APIRouter()


@userRouter.post("/predict/")
async def predict(file: UploadFile = File(...)):
    return await user_controller.predict(file)
