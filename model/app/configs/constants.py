from dotenv import load_dotenv
import os

load_dotenv()

from ultralytics import YOLO

model = YOLO("./runs/detect/train/weights/last.pt")

MONGO_URL = os.getenv("MONGO_URL")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
APP_API = os.getenv("APP_API")
