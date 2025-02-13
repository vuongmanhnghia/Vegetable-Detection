from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from app.utils.token_helper import verifyToken
from app.configs.database import users
from bson import ObjectId


async def require_authentication(request: Request):

    try:
        # Get token from request headers
        token = request.headers.get("Authorization")

        if token:

            # Tách chuỗi token
            token = token.split(" ")[1]
            user_id = await verifyToken(token)
            user = await users.find_one({"_id": ObjectId(user_id)})
            if user:
                request.current_user = user
                return
    except Exception as error:
        print(error)
        raise HTTPException(
            status_code=401, detail="Your session is expired, please login again"
        )
    raise HTTPException(status_code=401, detail="You need to login to access this page")
