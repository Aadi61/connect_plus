from api import app
from firebase.doctor_appointment import get_all_doctor_details

from flask import jsonify, request
from werkzeug.utils import secure_filename

# Retreive all doctor details
@app.route('/retreive_all_doctor_details', methods=['GET'])
def retreive_items():
    doctor_details = get_all_doctor_details()
    return jsonify(doctor_details)