from fastapi import APIRouter, File, UploadFile, Depends, Request
from app.controllers import user_controller
from app.middleware.require_authentication import require_authentication

userRouter = APIRouter()


@userRouter.post("/predict/")
async def predict(file: UploadFile = File(...)):
    return await user_controller.predict(file)


@userRouter.post("/save", dependencies=[Depends(require_authentication)])
async def save_image(image_url: str, request: Request):
    return await user_controller.save_image(image_url, request)


@userRouter.get("/history", dependencies=[Depends(require_authentication)])
async def get_history(request: Request):
    return await user_controller.get_history(request)
