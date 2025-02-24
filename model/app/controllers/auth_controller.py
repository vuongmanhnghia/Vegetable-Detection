from app.services import auth_service


async def get_me(user_id):
    result = await auth_service.profile(user_id)
    return {
        "status": 200,
        "success": True,
        "message": "OK",
        "data": result,
    }


async def google_login(token):
    result = await auth_service.google_login(token)
    return {
        "status": 200,
        "success": True,
        "message": "Login success!",
        "data": result,
    }
