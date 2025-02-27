from fastapi import Request, HTTPException
from app.configs.database import users
from bson import ObjectId


async def require_authentication(request: Request):
    try:
        user_id = request.headers.get("user_id")
        if user_id:
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
