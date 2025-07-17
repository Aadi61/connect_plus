from db import db
from bson import ObjectId

carpool_col = db["carpool"]

def add_carpool_details(data):
    data["time"] = int(data["time"])
    res = carpool_col.insert_one(data)
    carpool_col.update_one({"_id": res.inserted_id}, {"$set": {"carpool_id": str(res.inserted_id)}})
    return str(res.inserted_id)

def retrieve_carpool_list(data):
    start = int(data["time_slot"][:2]) * 100
    end = int(data["time_slot"][2:]) * 100
    matches = carpool_col.find({
        "time": {"$gte": start, "$lte": end},
        "destination": data["destination"]
    })
    return [{**doc, "_id": str(doc["_id"])} for doc in matches]
