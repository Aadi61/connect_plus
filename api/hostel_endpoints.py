from api import app
from firebase.hostel import add_rommie_details, retrieve_name_of_all_roomies
from firebase.lost_and_found import *

from flask import jsonify, request
from werkzeug.utils import secure_filename

# Add the user to the hostel database
@app.route('/add_rommie_details', methods=['POST'])
def add_roomie_user():
    room_type = request.form['room_type']
    bed_type = request.form['bed_type']
    block_name = request.form['block_name']
    user_id = request.form['user_id']

    add_rommie_details(room_type, bed_type, block_name, user_id)
    return jsonify({'message': 'User added successfully'})

# Retrieve the name of all roomies in a specific room
@app.route('/retrieve_name_of_all_roomies', methods=['POST'])
def retrieve_roomies():
    print(request.get_json())
    room_type = request.get_json()['room_type']
    bed_type = request.get_json()['bed_type']
    block_name = request.get_json()['block_name']

    roomies = retrieve_name_of_all_roomies(room_type, block_name, bed_type)
    return jsonify(roomies)