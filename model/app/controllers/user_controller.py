from app.services import user_service


async def predict(file):
    result = await user_service.predict(file)
    return {
        "status": 200,
        "success": True,
        "message": "Success!",
        "data": result,
    }
