from flask import Blueprint, request, jsonify, send_from_directory
from logic import *

lostfound_bp = Blueprint('lostfound', __name__)
print(__name__)
print("Hello")
@lostfound_bp.route('/lostfound/add_found_item', methods=['POST'])
def add_item():
    form = request.form
    image_file = request.files['image']

    image_url = upload_to_s3(image_file)
    if not image_url:
        return jsonify({"error": "Image upload failed"}), 500

    add_found_item(
        form['name'], image_url, form['place'],
        form['contact'], form['user_id'], form['date_found']
    )
    return jsonify({"message": "Item added successfully", "image_url": image_url})



@lostfound_bp.route('/lostfound/retreive_all_found_items', methods=['GET'])
def retreive_found_items():
    return jsonify(retreive_all_found_items())


@lostfound_bp.route('/lostfound/retreive_found_item_user', methods=['POST'])
def retreive_item_user():
    user_id = request.get_json()['user_id']
    return jsonify(retreive_found_item(user_id))


@lostfound_bp.route('/lostfound/delete_found_item', methods=['POST'])
def delete_found():
    found_id = request.get_json()['found_id']
    delete_found_item(found_id)
    return jsonify({"message": "Item deleted successfully"})


@lostfound_bp.route('/lostfound/add_lost_item', methods=['POST'])
def add_lost():
    form = request.form
    image_file = request.files['image']

    image_url = upload_to_s3(image_file)
    if not image_url:
        return jsonify({"error": "Image upload failed"}), 500

    lost_id = add_lost_item(
        form['name'], image_url,
        form['place'], form['contact'],
        form['user_id'], form['date_lost']
    )
    return jsonify({"message": "Lost item added successfully", "lost_id": lost_id})



@lostfound_bp.route('/lostfound/retreive_all_lost_items', methods=['GET'])
def retrieve_all_lost():
    return jsonify(retreive_all_lost_items())


@lostfound_bp.route('/lostfound/retrieve_lost_items_user', methods=['POST'])
def retrieve_lost_user():
    user_id = request.get_json()['user_id']
    return jsonify(retrieve_lost_item(user_id))


@lostfound_bp.route('/lostfound/mark_returned', methods=['POST'])
def mark_item_as_returned_route():
    item_id = request.get_json()['item_id']
    success = mark_item_as_returned2(item_id)
    return jsonify({'success': success})
