from api import app
from firebase.carpooling import add_carpool_details, retrieveList
from firebase.lost_and_found import *

from flask import jsonify, request
from werkzeug.utils import secure_filename

# Add carpooling details to the database
@app.route('/add_carpooling_details', methods=['POST'])
def add_carpooling_details_route():
    name = request.form['name']
    contact = request.form['contact']
    time = request.form['time']
    destination = request.form['destination']

    carpool_id = add_carpool_details(name, contact, time, destination)
    return jsonify({'message': 'Carpooling details added successfully', 'carpool_id': carpool_id})

# Retrieve carpooling details
@app.route('/retrieve_carpooling_details', methods=['POST'])
def retrieve_carpooling_details_route():
    print(request.get_json())
    time_slot = request.get_json()['time_slot']
    destination = request.get_json()['destination']

    carpool_matches = retrieveList(time_slot, destination)
    return jsonify(carpool_matches)
