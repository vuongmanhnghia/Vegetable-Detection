from bcrypt import checkpw


def verify_password(password, hashed_password):
    return checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
