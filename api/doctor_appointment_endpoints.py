from api import app
from connect_plus.firebase.lost_and_found import save_image_to_firebase
from firebase.doctor_appointment import add_doctor_detail, add_user_detail, get_all_doctor_details, retreiveTimeList

from flask import jsonify, request
from werkzeug.utils import secure_filename

# Retreive all doctor details
@app.route('/retreive_all_doctor_details', methods=['GET'])
def retreive_items():
    doctor_details = get_all_doctor_details()
    return jsonify(doctor_details)

#Add doctor details
@app.route('/add_doctor_detail', methods=['POST'])
def add_doctor():
    name = request.form['name']
    venue = request.form['venue']
    type = request.form['type']
    slots = request.form['slots']

    add_doctor_detail(name, venue, type, slots)
    return jsonify({'message': 'Item added successfully'})  

# Retreive all doctor details of a particular doctor at a particular date
@app.route('/retreiveTimeList', methods=['POST'])
def retreive_time_list():
    doctor_id = request.get_json()['doctor_id']
    date = request.get_json()['date']
    timingsList = retreiveTimeList(doctor_id, date)
    return jsonify(timingsList)

# Retreive all doctor details
@app.route('/retreive_all_doctor_details', methods=['GET'])
def retreive_items():
    doctor_details = get_all_doctor_details()
    return jsonify(doctor_details)

# Book an appointment
@app.route('/book', methods=['POST'])
def book():
    date = request.get_json()['date']
    time = request.get_json()['time']
    doctor_id = request.get_json()['doctor_id']
    user_id = request.get_json()['user_id']
    book(date, time, doctor_id, user_id)
    return jsonify({'message': 'Appointment booked successfully'})

# Add user details
@app.route('/add_user_detail', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    appointment_history = request.form['appointment_history']
    add_user_detail(name, email, password, appointment_history)
    return jsonify({'message': 'User added successfully'})

