from datetime import timedelta
from app.configs.database import users
from app.schemas.user_schemas import details_user
from app.utils.token_helper import generate_token, decode_token
from google.oauth2 import id_token
from google.auth.transport import requests

from app.configs.constants import GOOGLE_CLIENT_ID


async def auth_token(user):
    access_token = await generate_token(
        {"user_id": user["_id"]}, expires_in=timedelta(hours=1)
    )
    decode = await decode_token(access_token)
    expireIn = decode["exp"]
    return {
        "access_token": access_token,
        "expire_in": expireIn,
        "auth_type": "Bearer Token",
    }


async def profile(request):
    user = await users.find_one({"_id": request.state.user["_id"]})
    user["_id"] = str(user["_id"])
    user["created_at"] = user["created_at"]
    user["updated_at"] = user["updated_at"]
    return details_user(user)


async def google_login(token):
    # Xác thực token từ Google
    id_info = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)

    # Kiểm tra xem token có hợp lệ không
    email, name, picture, sub = (
        id_info.get("email"),
        id_info.get("name", ""),
        id_info.get("picture", ""),
        id_info.get("sub"),
    )

    account = await users.find_one({"email": email, "google_id": sub})
    if not account:
        account = {
            "email": email,
            "name": name,
            "avatar": picture,
            "google_id": sub,
        }
        print("account", account)
        print("type", type(account))
        await users.insert_one(account)
    print("account", account)
    account["_id"] = str(account["_id"])
    return account
