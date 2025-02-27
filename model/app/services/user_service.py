from fastapi import UploadFile, File, HTTPException
from bson import ObjectId
from app.configs.constants import model, APP_API
from PIL import Image, UnidentifiedImageError
from app.configs.database import histories
from app.schemas.history_schemas import list_history
from uuid import uuid4
import io
import os


async def upload_image(file: UploadFile = File(...), processed_image=None):
    try:
        file_extension = file.filename.split(".")[-1]
        file_name = f"{uuid4()}.{file_extension}"

        if processed_image:

            file_path = os.path.join("public/images", file_name)
            processed_image.save(file_path)
        else:
            file_content = await file.read()
            os.makedirs("public/images", exist_ok=True)  # Tạo thư mục nếu chưa tồn tại
            file_path = os.path.join("public/images", file_name)
            with open(file_path, "wb") as f:
                f.write(file_content)
        image_url = f"/public/images/{file_name}"
        return image_url
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
        results = results[0]

    result_image_path = "result_image.jpg"
    results.save(result_image_path)

    image_url = await upload_image(file, processed_image=results)

    return APP_API + image_url


async def save_image(image_url: str, user):
    image_url_format = image_url.replace(APP_API, "")
    await histories.insert_one(
        {"user_id": (ObjectId(user["_id"])), "image_url": image_url_format}
    )


async def get_history(user):
    result = await histories.find({"user_id": user["_id"]}).to_list(length=None)
    return list_history(result)
