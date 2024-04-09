from api import app
from firebase.lost_and_found import *

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

    add_found_item(name, place, contact, user_id)  
    return jsonify({'message': 'Item added successfully'})  
    
# Retreive all found items of a user
@app.route('/retreive_found_item_user', methods=['POST'])
def retreive_item_user():
    found_items_list = retreive_found_item(request.get_json()['user_id'])
    return jsonify(found_items_list)



# Delete a specific found item
@app.route('/delete_found_item', methods=['POST'])
def delete_found():
    req_data = request.get_json()
    print(req_data)
    found_id = req_data['found_id']
    delete_found_item(found_id)
    print('inside')
    print(found_id)
    return jsonify({'message': 'Item deleted successfully'})

@app.route('/delete_lost_item', methods=['POST'])
def delete_lost():
    req_data = request.get_json()
    print(req_data)
    lost_id = req_data['found_id']
    delete_found_item(lost_id)
    print('inside')
    print(lost_id)
    return jsonify({'message': 'Item deleted successfully'})


# Add a lost item
@app.route('/add_lost_item', methods=['POST'])
def add_lost():
    req_data = request.get_json()
    name = req_data['name']
    image_url = req_data['image_url']
    place = req_data['place']
    contact = req_data['contact']
    user_id = req_data['user_id']
    
    lost_id = add_lost_item(name, image_url, place, contact, user_id)
    return jsonify({'message': 'Lost item added successfully', 'lost_id': lost_id})



# Retrieve all lost items
@app.route('/retreive_all_lost_items', methods=['GET'])
def retrieve_all_lost():
    lost_items_list = retreive_all_lost_items()
    return jsonify(lost_items_list)




# Retrieve lost items for a specific user
@app.route('/retrieve_lost_items_user', methods=['POST'])
def retrieve_lost_user():
    user_id = request.get_json()['user_id']
    lost_items_list = retrieve_lost_item(user_id)
    return jsonify(lost_items_list)



# Mark an item as returned
@app.route('/mark_returned', methods=['POST'])
def mark_item_as_returned():
    item_id = request.json.get('item_id')
    success = mark_item_as_returned2(item_id)
    return jsonify({'success': success})