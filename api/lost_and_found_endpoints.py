from api import app
from firebase.lost_and_found import retreive_all_found_items, add_found_item, retreive_found_item

from flask import jsonify, request


@app.route('/retreive_all_found_items', methods=['GET'])
def retreive_items():
    found_items_list = retreive_all_found_items()
    return jsonify(found_items_list)

@app.route('/add_found_item', methods=['POST'])
def add_item():
    req_data = request.get_json()
    add_found_item(req_data['name'],req_data['image_url'],req_data['place'],req_data['contact'],req_data('user_id'))
    
    
@app.route('/retreive_found_item_user', methods=['POST'])
def retreive_item_user():
    # found_items_list = retreive_found_item(request.get_json()['user_id'])
    # return jsonify(found_items_list)
    print('printing  ')
    print(request.get_json()['user_id'])
    found_items_list = retreive_found_item(request.get_json()['user_id'])
    return jsonify(found_items_list)