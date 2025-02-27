from app.services import user_service


async def predict(file):
    result = await user_service.predict(file)
    return {
        "status": 200,
        "success": True,
        "message": "Success!",
        "data": result,
    }


async def save_image(image_url, request):
    await user_service.save_image(image_url, request.current_user)
    return {
        "status": 200,
        "success": True,
        "message": "Success!",
    }


async def get_history(request):
    result = await user_service.get_history(request.current_user)
    return {
        "status": 200,
        "success": True,
        "message": "Success!",
        "data": result,
    }
