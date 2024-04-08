from __init__ import db

found_collection = "found"


found_ref = db.collection('found').document()


def add_found_item(name, image_url, place,contact,user_id):
    found_ref = db.collection(found_collection).document()
    
    found_ref.set({
        "name":name,
        "image_url":image_url,
        "place":place,
        "contact":contact,
        "user_id":user_id,
    })
    found_id= found_ref.id

    found_ref.update({
        "found_id":found_id
    })
    print("Founded item added successfully with ID:", found_id)
    

def retreive_found_item(found_id):
    found_ref = db.collection(found_collection).document(found_id)
    found_item = found_ref.get()
    if found_item.exists:
        return found_item.to_dict()
    else:
        return None

def retreive_all_found_items():
    found_ref = db.collection(found_collection)
    found_items = found_ref.get()
    print("found items: ",found_items)
    found_items_list = []
    for found_item in found_items:
        found_items_list.append(found_item.to_dict())
    return found_items_list
