def details_user(user):
    return {
        "_id": str(user["_id"]),
        "email": user["email"],
        "name": user["name"],
        "avatar": user["avatar"],
        "google_id": user["google_id"],
    }


def user_id(user):
    return {"_id": user["_id"]}


def list_users(users):
    return [details_user(user) for user in users]


# Compare this snippet from app/controllers/user_controller.py:
