from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
from PIL import Image, UnidentifiedImageError
import io
from fastapi.responses import StreamingResponse

app = FastAPI()

model = YOLO("./runs/detect/train/weights/last.pt")


@app.post("/predict/")
async def predict(file: UploadFile = File(...)):

    # Read image data
    image_data = await file.read()

    print(f"File size: {len(image_data)} bytes")

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

    # Return the image as a response
    return StreamingResponse(open(result_image_path, "rb"), media_type="image/jpeg")
