from db.operations import OpsForMongo
from dotenv import load_dotenv
import motor.motor_asyncio
import os

load_dotenv()
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGO_CONNECTION_STRING"])
db = client.mflix

def get_movie_ops():
    return OpsForMongo(db, "movies")