from flask import Blueprint, request, jsonify, send_from_directory
from logic import *

lostfound_bp = Blueprint('lostfound', __name__)

@lostfound_bp.route('/uploads/<filename>')
def serve_file(filename):
    return send_from_directory('uploads', filename)

@lostfound_bp.route('/add_found_item', methods=['POST'])
def add_item():
    form = request.form
    image_file = request.files['image']
    image_url = save_image_locally(image_file)

    add_found_item(
        form['name'], image_url, form['place'],
        form['contact'], form['user_id'], form['date_found']
    )
    return jsonify({"message": "Item added successfully"})


@lostfound_bp.route('/retreive_all_found_items', methods=['GET'])
def retreive_found_items():
    return jsonify(retreive_all_found_items())


@lostfound_bp.route('/retreive_found_item_user', methods=['POST'])
def retreive_item_user():
    user_id = request.get_json()['user_id']
    return jsonify(retreive_found_item(user_id))


@lostfound_bp.route('/delete_found_item', methods=['POST'])
def delete_found():
    found_id = request.get_json()['found_id']
    delete_found_item(found_id)
    return jsonify({"message": "Item deleted successfully"})


@lostfound_bp.route('/add_lost_item', methods=['POST'])
def add_lost():
    data = request.get_json()
    lost_id = add_lost_item(
        data['name'], data['image_url'],
        data['place'], data['contact'],
        data['user_id'], data['date_lost']
    )
    return jsonify({"message": "Lost item added successfully", "lost_id": lost_id})


@lostfound_bp.route('/retreive_all_lost_items', methods=['GET'])
def retrieve_all_lost():
    return jsonify(retreive_all_lost_items())


@lostfound_bp.route('/retrieve_lost_items_user', methods=['POST'])
def retrieve_lost_user():
    user_id = request.get_json()['user_id']
    return jsonify(retrieve_lost_item(user_id))


@lostfound_bp.route('/mark_returned', methods=['POST'])
def mark_item_as_returned_route():
    item_id = request.get_json()['item_id']
    success = mark_item_as_returned2(item_id)
    return jsonify({'success': success})
