from fastapi import HTTPException
from datetime import datetime, timedelta
from app.configs.database import users
from app.schemas.user_schemas import details_user, user_id
from app.utils.verify_password import verify_password
from app.utils.token_helper import generate_token, decode_token
from bson import ObjectId

# AuthService
async def register(user):
    # Kiểm tra xem email đã tồn tại chưa
    if await users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already exists")

    now = datetime.utcnow()

    user = user.dict(by_alias=True)
    user.pop("_id", None)
    user["created_at"] = now
    user["updated_at"] = now

    try:
        result = await users.insert_one(user)
        user["_id"] = str(result.inserted_id)
        return details_user(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def login(current_user):
    try:
        user = await users.find_one({"email": current_user.email})
        # Verify password
        if user and verify_password(current_user.password, user["password"]):
            user["_id"] = str(user["_id"])
            return user_id(user)
        raise HTTPException(status_code=500, detail="Email or password is incorrect")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


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


async def update_profile(current_user, user):

    user = user.dict(by_alias=True)
    user["updated_at"] = datetime.utcnow()
    user = await users.find_one_and_update(
        {"_id": current_user["_id"]}, {"$set": user}, return_document=True
    )
    if user:
        user["_id"] = str(user["_id"])
        user["created_at"] = user["created_at"]
        user["updated_at"] = user["updated_at"]
        user["_id"] = id
        return details_user(user)
    raise HTTPException(status_code=404, detail="User not found")


async def delete_user(current_user):
    result = await users.delete_one({"_id": current_user["_id"]})
    if result.deleted_count:
        return
    raise HTTPException(status_code=404, detail="User not found")


async def get_me(current_user):
    user = await users.find_one({"_id": current_user["_id"]})
    user["_id"] = str(user["_id"])
    user["created_at"] = user["created_at"]
    user["updated_at"] = user["updated_at"]

    return details_user(user)


async def change_password(current_user, password):
        user = await users.find_one({"_id": current_user["_id"]})
        if user and verify_password(password.old_password, user["password"]):
            result = await users.update_one(
                {"_id": current_user["_id"]},
                {"$set": {"password": password.new_password}},
            )
            if result.modified_count:
                return
        raise HTTPException(status_code=500, detail="Change password failed")

async def change_password_by_id(current_user, password, id: str):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can change other users' password")
    user = await users.find_one({"_id": ObjectId(id)}) 
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user["role"] == "admin":
        raise HTTPException(status_code=403, detail="Admin cannot change password of another admin")
    result = await users.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"password": password.new_password}},
    )
    if result.modified_count:
        return {"message": "Password updated successfully"}
    else:
        raise HTTPException(status_code=500, detail="Change password failed")
    



