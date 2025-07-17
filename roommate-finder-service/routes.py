from flask import request, jsonify
from logic import add_rommie_details, retrieve_name_of_all_roomies
from flask import Blueprint

hostel_bp = Blueprint('hostel', __name__)

@hostel_bp.route('/hostel/add_rommie_details', methods=['POST'])
def add_roomie_user():
    form = request.form
    room_type = form['room_type']
    bed_type = form['bed_type']
    block_name = form['block_name']
    user_id = form['user_id']

    add_rommie_details(room_type, bed_type, block_name, user_id)
    return jsonify({'message': 'User added successfully'})


@hostel_bp.route('/hostel/retrieve_name_of_all_roomies', methods=['POST'])
def retrieve_roomies():
    data = request.get_json()
    room_type = data['room_type']
    bed_type = data['bed_type']
    block_name = data['block_name']

    roomies = retrieve_name_of_all_roomies(room_type, block_name, bed_type)
    return jsonify(roomies)
