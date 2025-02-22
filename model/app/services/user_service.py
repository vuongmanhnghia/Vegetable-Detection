from fastapi import UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from app.configs.constants import model
from PIL import Image, UnidentifiedImageError
from uuid import uuid4
import io
import os


async def upload_image(file: UploadFile = File(...), processed_image=None):
    try:
        # Tạo tên file duy nhất (UUID) để tránh trùng lặp
        file_extension = file.filename.split(".")[-1]  # Lấy phần mở rộng của file
        file_name = f"{uuid4()}.{file_extension}"

        # Nếu không có ảnh đã xử lý, sử dụng ảnh gốc
        if processed_image:
            # Nếu có ảnh đã xử lý, lưu ảnh đã xử lý vào thư mục
            file_path = os.path.join("public/images", file_name)
            processed_image.save(file_path)  # Lưu ảnh đã xử lý
        else:
            # Đọc nội dung file gốc và lưu vào thư mục
            file_content = await file.read()
            os.makedirs("public/images", exist_ok=True)  # Tạo thư mục nếu chưa tồn tại
            file_path = os.path.join("public/images", file_name)
            with open(file_path, "wb") as f:
                f.write(file_content)

        # Lưu đường dẫn vào cơ sở dữ liệu MongoDB hoặc trả về đường dẫn cho client
        image_url = (
            f"/public/images/{file_name}"  # Đường dẫn ảnh sẽ được trả về cho client
        )
        return image_url
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def predict(file: UploadFile):
    # Đọc ảnh từ file
    image_data = await file.read()

    try:
        image = Image.open(io.BytesIO(image_data))
    except UnidentifiedImageError:
        return {
            "error": "Unable to identify image format. Please upload a valid image."
        }
    except Exception as e:
        return {"error": f"An error occurred while processing the image: {str(e)}"}

    # Giả sử bạn đã có mô hình để chạy dự đoán trên ảnh
    results = model(image)  # Giả sử bạn có mô hình dự đoán đã được nạp
    if isinstance(results, list):
        results = results[0]  # Nếu kết quả là list, lấy phần tử đầu tiên

    # Lưu ảnh kết quả
    result_image_path = "result_image.jpg"
    results.save(result_image_path)

    # Gọi hàm upload_image để lưu ảnh đã xử lý và lấy đường dẫn
    image_url = await upload_image(file, processed_image=results)

    # Trả về đường dẫn ảnh đã xử lý cho client
    return image_url
