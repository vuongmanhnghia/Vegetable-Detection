from motor.motor_asyncio import AsyncIOMotorClient
from app.configs.constants import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)

db = client["VegetableDetection"]

users = db["users"]
histories = db["histories"]
