from app.configs.database import users
from bson import ObjectId
from app.services import auth_service


async def register(user):
    result = await auth_service.register(user)
    return {
        "status": 201,
        "success": True,
        "message": "Create new user success!",
        "data": result,
    }


async def login(user):
    valid_login = await auth_service.login(user)
    result = await auth_service.auth_token(valid_login)
    return {
        "status": 200,
        "success": True,
        "message": "Login success!",
        "data": result,
    }


async def profile(request):
    result = await auth_service.profile(request)
    return {
        "status": 200,
        "success": True,
        "message": "OK",
        "data": result,
    }


async def update_profile(request, user):
    result = await auth_service.update_profile(request.current_user, user)
    return {
        "status": 200,
        "success": True,
        "message": "Update user success!",
        "data": result,
    }


async def delete_user(request):
    await auth_service.delete_user(request.current_user)
    return {
        "status": 200,
        "success": True,
        "message": "Delete user success!",
    }


async def get_me(request):
    result = await auth_service.get_me(request.current_user)
    return {
        "status": 200,
        "success": True,
        "message": "OK",
        "data": result,
    }


async def change_password(request, password):
    result = await auth_service.change_password(request.current_user, password)
    return {
        "status": 200,
        "success": True,
        "message": "Change password success!",
    }

async def change_password_by_id(request, password, id):
    result = await auth_service.change_password_by_id(request.current_user, password, id)
    return {
        "status": 200,
        "success": True,
        "message": "Change password success!",
    }