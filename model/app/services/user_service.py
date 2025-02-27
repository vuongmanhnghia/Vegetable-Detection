from fastapi import UploadFile, File, HTTPException
from bson import ObjectId
from app.configs.constants import model, APP_API
from PIL import Image, UnidentifiedImageError
from app.configs.database import histories
from app.schemas.history_schemas import list_history
from uuid import uuid4
from datetime import datetime
import shutil
import io
import os


SAVE_DIRECTORY = "public/images"
SAVE_FILENAME = "processed_image.jpg"
os.makedirs(SAVE_DIRECTORY, exist_ok=True)  # Đảm bảo thư mục tồn tại


async def upload_image(file_content, processed_image=None):
    try:
        os.makedirs(SAVE_DIRECTORY, exist_ok=True)  # Đảm bảo thư mục tồn tại
        file_path = os.path.join(SAVE_DIRECTORY, SAVE_FILENAME)

        if processed_image:
            processed_image.save(file_path)
        else:
            with open(file_path, "wb") as f:
                f.write(file_content)

        return f"/{SAVE_DIRECTORY}/{SAVE_FILENAME}"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def predict(file: UploadFile):
    image_data = await file.read()

    try:
        image = Image.open(io.BytesIO(image_data))
    except UnidentifiedImageError:
        return {
            "error": "Unable to identify image format. Please upload a valid image."
        }
    except Exception as e:
        return {"error": f"An error occurred while processing the image: {str(e)}"}

    results = model(image)
    if isinstance(results, list):
        if not results:  # Nếu danh sách rỗng
            return {"error": "No detections found in the image."}
        results = results[0]

    if hasattr(results, "boxes") and len(results.boxes) == 0:
        return {"error": "No objects detected in the image."}

    result_image_path = "result_image.jpg"
    results.save(result_image_path)

    image_url = await upload_image(file, processed_image=results)

    return APP_API + image_url


async def save_image(image_url: str, user):

    filename = f"{user['_id']}_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
    new_image_path = os.path.join(SAVE_DIRECTORY, filename)

    image_url_format = image_url.replace(APP_API, "")
    image_url_format = os.path.join(os.getcwd(), image_url_format.lstrip("/"))
    if not os.path.exists(image_url_format):
        raise FileNotFoundError(f"Image file not found: {image_url_format}")
    shutil.copy(image_url_format, new_image_path)

    await histories.insert_one(
        {"user_id": ObjectId(user["_id"]), "image_url": f"/{SAVE_DIRECTORY}/{filename}"}
    )

    return f"/{SAVE_DIRECTORY}/{filename}"


async def get_history(user):
    result = await histories.find({"user_id": user["_id"]}).to_list(length=None)
    return list_history(result)
