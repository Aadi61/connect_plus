from flask import Blueprint, request, jsonify
from logic import *

appointment_bp = Blueprint('appointment', __name__)

@appointment_bp.route('/appointment/add_doctor_detail', methods=['POST'])
def add_doctor_route():
    form = request.form
    add_doctor_detail(form['name'], form['venue'], form['type'], form['slots'])
    return jsonify({'message': 'Doctor added successfully'})

@appointment_bp.route('/appointment/add_user_detail', methods=['POST'])
def add_user_route():
    form = request.form
    add_user_detail(form['name'], form['email'], form['password'], form['appointment_history'])
    return jsonify({'message': 'User added successfully'})

@appointment_bp.route('/appointment/retreive_all_doctor_details', methods=['GET'])
def get_doctors_route():
    return jsonify(get_all_doctor_details())

@appointment_bp.route('/appointment/retreiveTimeList', methods=['POST'])
def get_timeslot_route():
    data = request.get_json()
    return jsonify(retreiveTimeList(data['doctor_id'], data['date']))

@appointment_bp.route('/appointment/book', methods=['POST'])
def book_route():
    data = request.get_json()
    appointment_id = book(data['date'], data['time'], data['doctor_id'], data['user_id'])
    return jsonify({'message': 'Appointment booked successfully', 'appointment_id': appointment_id})

@appointment_bp.route('/appointment/get_appointment_history', methods=['POST'])
def get_history_route():
    data = request.get_json()
    return jsonify(getHistory(data['user_id']))
