from api import app
from firebase.lost_and_found import retreive_all_found_items, add_found_item, retreive_found_item, save_image_to_firebase

from flask import jsonify, request
from werkzeug.utils import secure_filename



# Retreive all found items
@app.route('/retreive_all_found_items', methods=['GET'])
def retreive_items():
    found_items_list = retreive_all_found_items()
    return jsonify(found_items_list)


# Add a found item
@app.route('/add_found_item', methods=['POST'])
def add_item():
    name = request.form['name']
    place = request.form['place']
    contact = request.form['contact']
    user_id = request.form['user_id']

    image = request.files['image']
    filename = secure_filename(image.filename)
    image.save(filename)
    image_url = save_image_to_firebase(filename)
    add_found_item(name, image_url, place, contact, user_id)  
    return jsonify({'message': 'Item added successfully'})  
    
# Retreive all found items of a user
@app.route('/retreive_found_item_user', methods=['POST'])
def retreive_item_user():
    found_items_list = retreive_found_item(request.get_json()['user_id'])
    return jsonify(found_items_list)
