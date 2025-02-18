from fastapi import APIRouter, Request, Depends, HTTPException, Header
from app.controllers import auth_controller
from app.models.user import (
    UserLogin,
    UserRegister,
    UserUpdate,
    UserChangePassword,
    ChangePasswordByAdmin,
)
from app.middleware.require_authentication import require_authentication
import httpx

authRouter = APIRouter()


# Đăng ký tài khoản
@authRouter.post("/register")
async def register(user: UserRegister):
    return await auth_controller.register(user)


@authRouter.post("/google")
async def google_login(token: str):
    return await auth_controller.google_login(token)


# Đăng nhập
@authRouter.post("/login")
async def login(user: UserLogin):
    return await auth_controller.login(user)


# Cập nhật thông tin tài khoản theo ID
@authRouter.put("/", dependencies=[Depends(require_authentication)])
async def update_profile(request: Request, user: UserUpdate):
    return await auth_controller.update_profile(request, user)


# Xoá tài khoản theo ID
@authRouter.delete("/", dependencies=[Depends(require_authentication)])
async def delete_user(request: Request):
    return await auth_controller.delete_user(request)


# Lấy thông tin tài khoản
@authRouter.get("/me", dependencies=[Depends(require_authentication)])
async def me(request: Request):
    return await auth_controller.get_me(request)


@authRouter.put("/change-password", dependencies=[Depends(require_authentication)])
async def change_password(request: Request, password: UserChangePassword):
    return await auth_controller.change_password(request, password)


@authRouter.put(
    "/change-password-by-id/{id}", dependencies=[Depends(require_authentication)]
)
async def change_password_by_id(
    request: Request, password: ChangePasswordByAdmin, id: str
):
    return await auth_controller.change_password_by_id(request, password, id)


GOOGLE_USER_INFO_URL = "https://www.googleapis.com/oauth2/v2/userinfo"


@authRouter.post("/google")
async def google_auth(request: Request):
    data = await request.json()  # Lấy dữ liệu JSON từ frontend
    token = data.get("token")

    if not token:
        raise HTTPException(status_code=422, detail="Token is missing")

    # Kiểm tra token và lấy thông tin người dùng
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://www.googleapis.com/oauth2/v2/userinfo",
            headers={"Authorization": f"Bearer {token}"},
        )

        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to fetch user info")

        user_info = response.json()

    return user_info
