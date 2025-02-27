def details_history(history):
    return {
        "_id": str(history["_id"]),
        "user_id": str(history["user_id"]),
        "image_url": history["image_url"],
    }


def list_history(histories):
    return [details_history(history) for history in histories]
