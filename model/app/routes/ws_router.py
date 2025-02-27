from fastapi import WebSocket, WebSocketDisconnect
from fastapi.routing import APIRouter
import cv2
import numpy as np
from PIL import Image
import io
import base64
import asyncio

wsRouter = APIRouter()

from app.configs.constants import model


async def process_frame(image_data):
    image_bytes = base64.b64decode(image_data)
    image = Image.open(io.BytesIO(image_bytes))

    results = model(image)

    if isinstance(results, list):
        if not results:  # Nếu danh sách rỗng
            return {"error": "No detections found in the image."}
        results = results[0]
    # Nếu không có phát hiện, trả về ảnh gốc
    if hasattr(results, "boxes") and len(results.boxes) == 0:
        return {"error": "No objects detected."}

    # Lưu ảnh kết quả
    result_image_path = "public/images/result.jpg"
    results.save(result_image_path)

    # Encode ảnh kết quả thành base64 để gửi về frontend
    with open(result_image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode("utf-8")

    return {"image": encoded_image}


@wsRouter.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()  # Nhận frame dạng base64 từ FE
            response = await process_frame(data)  # Xử lý ảnh
            await websocket.send_json(response)  # Gửi kết quả về FE
    except WebSocketDisconnect:
        print("Client disconnected")
