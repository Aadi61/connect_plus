from . import db

hostel_collection = "hostel"

def add_rommie_details(room_type, bed_type, block_name, user_id):
    room_ref = db.collection(hostel_collection).document()

    room_ref.set({
        "room_type": room_type,
        "bed_type": bed_type,
        "block_name": block_name,
        "user_id": user_id,
    })

    room_id = room_ref.id
    room_ref.update({"room_id": room_id})

def retrieve_name_of_all_roomies(room_type, block_name, bed_type):
    hostel_docs = db.collection(hostel_collection).get()
    name_of_all_roomies = []
    for hostel_doc in hostel_docs:
        hostel_dict = hostel_doc.to_dict()
        if (hostel_dict['room_type'] == room_type and 
            hostel_dict['block_name'] == block_name and 
            hostel_dict['bed_type'] == bed_type):
            name_of_all_roomies.append(hostel_dict)
    return name_of_all_roomies
