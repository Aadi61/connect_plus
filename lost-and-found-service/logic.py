import os
import uuid
from db import db

found_col = db["found"]
lost_col = db["lost"]

UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def save_image_locally(image_file):
    ext = image_file.filename.rsplit('.', 1)[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    path = os.path.join(UPLOAD_FOLDER, filename)
    image_file.save(path)
    return f"/uploads/{filename}"  # URL path for Flask to serve


def add_found_item(name, image_url, place, contact, user_id, date_found):
    doc = {
        "name": name,
        "image_url": image_url,
        "place": place,
        "contact": contact,
        "user_id": user_id,
        "date_found": date_found,
        "returned": False
    }
    result = found_col.insert_one(doc)
    found_col.update_one({"_id": result.inserted_id}, {"$set": {"found_id": str(result.inserted_id)}})


def retreive_found_item(user_id):
    return list(found_col.find({"user_id": user_id}, {"_id": 0}))


def retreive_all_found_items():
    return list(found_col.find({}, {"_id": 0}))


def delete_found_item(found_id):
    found_col.delete_one({"found_id": found_id})


def add_lost_item(name, image_url, place, contact, user_id, date_lost):
    doc = {
        "name": name,
        "image_url": image_url,
        "place": place,
        "contact": contact,
        "user_id": user_id,
        "date_lost": date_lost
    }
    result = lost_col.insert_one(doc)
    lost_col.update_one({"_id": result.inserted_id}, {"$set": {"lost_id": str(result.inserted_id)}})
    return str(result.inserted_id)


def retreive_all_lost_items():
    return list(lost_col.find({}, {"_id": 0}))


def retrieve_lost_item(user_id):
    return list(lost_col.find({"user_id": user_id}, {"_id": 0}))


def mark_item_as_returned2(found_id):
    result = found_col.update_one({"found_id": found_id}, {"$set": {"returned": True}})
    return result.modified_count > 0
