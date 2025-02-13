from app.configs.database import users
from app.services import user_service


async def get_user_by_email(email: str):
    result = await user_service.get_user_by_email(email)
    return {"status": 200, "success": True, "data": result}


async def get_all_users(request):
    query_params = request.query_params
    result = await user_service.get_all_users(query_params)
    return {"status": 200, "success": True, "data": result}


async def get_dashboard_data():
    result = await user_service.get_dashboard_data()
    return {
        "status": 200,
        "success": True,
        "message": "Dashboard data retrieved successfully",
        "data": result,
    }


async def predict(file):
    result = await user_service.predict(file)
    return result
