from db import db

hostel_col = db["hostel"]

def add_rommie_details(room_type, bed_type, block_name, user_id):
    doc = {
        "room_type": room_type,
        "bed_type": bed_type,
        "block_name": block_name,
        "user_id": user_id,
    }
    result = hostel_col.insert_one(doc)
    hostel_col.update_one({"_id": result.inserted_id}, {"$set": {"room_id": str(result.inserted_id)}})
    return str(result.inserted_id)


def retrieve_name_of_all_roomies(room_type, block_name, bed_type):
    query = {
        "room_type": room_type,
        "block_name": block_name,
        "bed_type": bed_type
    }
    roomies = list(hostel_col.find(query, {"_id": 0}))  # exclude _id
    return roomies
