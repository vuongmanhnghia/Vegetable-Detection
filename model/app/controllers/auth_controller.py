from app.services import auth_service


async def get_me(request):
    result = await auth_service.get_me(request.current_user)
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
