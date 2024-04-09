from . import db, bucket

found_collection = "found"



# Add a found itm to the database
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
    

# Retreive a particular user's found items
def retreive_found_item(user_id):
    found_ref = db.collection(found_collection)
    found_item = found_ref.get()
    print(found_item)
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
    print("found items: ",found_items)
    found_items_list = []
    for found_item in found_items:
        found_items_list.append(found_item.to_dict())
    return found_items_list


def save_image_to_firebase(filename):
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)
    blob.make_public()
    return blob.public_url
    