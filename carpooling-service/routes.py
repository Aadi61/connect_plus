from flask import Blueprint, request, jsonify
from logic import add_carpool_details, retrieve_carpool_list

carpool_bp = Blueprint('carpool', __name__)

@carpool_bp.route("/carpool/add", methods=["POST"])
def add():
    data = request.get_json()
    id = add_carpool_details(data)
    return jsonify({"carpool_id": id})

@carpool_bp.route("/carpool/retrieve", methods=["POST"])
def retrieve():
    data = request.get_json()
    matches = retrieve_carpool_list(data)
    return jsonify(matches)



