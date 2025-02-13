from fastapi import APIRouter, Request, Depends, HTTPException, File, UploadFile
from app.controllers import user_controller
from app.middleware.require_authentication import require_authentication

userRouter = APIRouter()


@userRouter.get("/", dependencies=[Depends(require_authentication)])
async def get_all_users(request: Request):
    user = request.current_user
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Only admin can get all users")
    return await user_controller.get_all_users(request)


@userRouter.get("/dashboard", dependencies=[Depends(require_authentication)])
async def get_dashboard_data(request: Request):
    user = request.current_user
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Only admin can get dashboard data")
    return await user_controller.get_dashboard_data()


@userRouter.post("/predict/")
async def predict(file: UploadFile = File(...)):
    return await user_controller.predict(file)
