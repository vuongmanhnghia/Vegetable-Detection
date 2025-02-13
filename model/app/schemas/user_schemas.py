def details_user(user):
    return {
        "email": user["email"],
        "full_name": user["full_name"],
        "phone_number": user["phone_number"],
        "avatar": user["avatar"],
        "date_of_birth": user["date_of_birth"],
        "address": user["address"],
        "gender": user["gender"],
        "role": user["role"],
    }


def user_id(user):
    return {"_id": user["_id"]}


def list_users(users):
    return [details_user(user) for user in users]


# Compare this snippet from app/controllers/user_controller.py:
