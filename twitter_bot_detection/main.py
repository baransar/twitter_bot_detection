from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
import joblib

app = FastAPI()

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

# load the pre-trained model
model = joblib.load("trained_model.pkl")

# connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["bot_classifier"]
collection = db["bot_results"]


class BotParams(BaseModel):
    screen_name: str
    description: str
    location: str
    verified: bool


@app.get('/classify_bots')
def classify_bots(screen_name: str, description: str, location: str, verified: bool):
    result = model.predict([[int('bot' in screen_name.lower()), 
                             int('bot' in description.lower()), 
                             int(location is None), 
                             int(not verified)]])[0]
    is_bot = not bool(result)
    existing_result = collection.find_one({"screen_name": screen_name, "description": description, "location": location, "verified": verified})
    if existing_result:
        collection.update_one({"_id": existing_result["_id"]}, {"$set": {"is_bot": is_bot}})
        return JSONResponse(content={"id": str(existing_result["_id"]), "is_bot": is_bot})
    else:
        result_data = {"screen_name": screen_name, "description": description, "location": location, "verified": verified, "is_bot": is_bot}
        inserted_id = collection.insert_one(result_data).inserted_id
        return JSONResponse(content={"id": str(inserted_id), "is_bot": is_bot})


@app.get('/bot_results/{id}')
def get_bot_result(id: str):
    result = collection.find_one({"_id": ObjectId(id)})
    if result:
        result["_id"] = str(result["_id"]) # convert ObjectId to string
        return JSONResponse(content=result)
    else:
        return JSONResponse(content={"error": "Result not found"}, status_code=404)



@app.get('/bot_ids')
def get_bot_ids():
    results = collection.find({}, {"_id": 1})
    ids = [str(result["_id"]) for result in results]
    return JSONResponse(content={"ids": ids})