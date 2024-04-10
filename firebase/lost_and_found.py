from . import db, bucket

found_collection = "found"

lost_collection = "lost"

# Add a found itm to the database
def add_found_item(name, image_url, place,contact,user_id,date):
    found_ref = db.collection(found_collection).document()
    
    found_ref.set({
        "name":name,
        "image_url":image_url,
        "place":place,
        "contact":contact,
        "user_id":user_id,
        "date_found":date
    })
    found_id= found_ref.id

    found_ref.update({
        "found_id":found_id
    })
    

# Retreive a particular user's found items
def retreive_found_item(user_id):
    found_ref = db.collection(found_collection)
    found_item = found_ref.get()
    found_items_list = []
    for item in found_item:
        dict_item = item.to_dict()
        if dict_item['user_id'] == user_id:
            print(dict_item)
            found_items_list.append(dict_item)
        
    return found_items_list


# Retreive all found items
def retreive_all_found_items():
    found_ref = db.collection(found_collection)
    found_items = found_ref.get()
    found_items_list = []
    for found_item in found_items:
        found_items_list.append(found_item.to_dict())
    return found_items_list


def save_image_to_firebase(image, filename):
    blob = bucket.blob(filename)
    blob.upload_from_file(image)
    blob.make_public()
    return blob.public_url

# Delete a specific item using found_id
def delete_found_item(found_id):
    found_ref = db.collection(found_collection).document(found_id)
    print(found_ref)
    found_ref.delete()
    
    
    
# Delete a specific item using lost_id
def delete_item(lost_id):
    found_ref = db.collection(lost_collection).document(lost_id)
    found_ref.delete()
    return True



# Add a lost item to the database
def add_lost_item(name, image_url, place, contact, user_id, date_lost):
    lost_ref = db.collection(lost_collection).document()
    lost_ref.set({
        "name": name,
        "image_url": image_url,
        "place": place,
        "contact": contact,
        "user_id": user_id,
        "date_lost": date_lost,  # Changed field name to date_lost
    })
    lost_id = lost_ref.id
    lost_ref.update({"lost_id": lost_id})  # Changed field name to lost_id
    return lost_id
    
    
# Retrieve all lost items
def retreive_all_lost_items():
    lost_ref = db.collection(lost_collection)
    lost_items = lost_ref.get()
    print("lost items: ", lost_items)
    lost_items_list = []
    for lost_item in lost_items:
        lost_items_list.append(lost_item.to_dict())
    return lost_items_list



# Retreive a particular user's lost items
def retrieve_lost_item(user_id):
    lost_ref = db.collection(lost_collection)
    lost_item = lost_ref.get()
    print(lost_item)
    lost_items_list = []
    for item in lost_item:
        dict_item = item.to_dict()
        if dict_item['user_id'] == user_id:
            print(dict_item)
            lost_items_list.append(dict_item)
    return lost_items_list



# Mark an item as returned
def mark_item_as_returned2(found_id):
    found_ref = db.collection(found_collection).document(found_id)
    found_ref.update({"returned": True})
    return True


