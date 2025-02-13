from fastapi import HTTPException
import jwt
from datetime import datetime
from dotenv import load_dotenv
import os


load_dotenv()


async def generate_token(
    data,
    expires_in,
):
    try:
        if not isinstance(data, dict):
            raise ValueError("Data phải là một dictionary")
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_in
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm="HS256")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def decode_token(token):
    try:
        return jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def verifyToken(token):
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
        return payload.get("user_id")
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
