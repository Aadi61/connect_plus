from db import doctor_col, user_col, appointment_col
from bson import ObjectId
import json

DEFAULT_IMAGE_URL = "https://www.shutterstock.com/image-photo/healthcare-medical-staff-concept-portrait-600nw-2281024823.jpg"

def add_doctor_detail(name, venue, type, slots):
    doc = {
        "name": name,
        "venue": venue,
        "type": type,
        "slots": json.loads(slots),  # Assuming slots is a stringified list of dicts
        "image_url": DEFAULT_IMAGE_URL
    }
    result = doctor_col.insert_one(doc)
    doctor_col.update_one({"_id": result.inserted_id}, {"$set": {"doctor_id": str(result.inserted_id)}})
    return str(result.inserted_id)

def add_user_detail(name, email, password, appointment_history):
    doc = {
        "name": name,
        "email": email,
        "password": password,
        "appointment_history": eval(appointment_history) if appointment_history else []
    }
    result = user_col.insert_one(doc)
    user_col.update_one({"_id": result.inserted_id}, {"$set": {"user_id": str(result.inserted_id)}})
    return str(result.inserted_id)

def get_all_doctor_details():
    doctors = doctor_col.find()
    doctor_list = []
    for d in doctors:
        doctor_list.append({
            "name": d["name"],
            "venue": d["venue"],
            "type": d["type"],
            "image_url": d["image_url"],
            "doctor_id": d["doctor_id"]
        })
    return doctor_list

def retreiveTimeList(doctor_id, date):
    doctor = doctor_col.find_one({"doctor_id": doctor_id})
    slots = doctor.get("slots", [])
    date_index = int(date) - 1
    time_slots = slots[date_index]
    return [int(hour) for hour, available in time_slots.items() if available > 0]

def book(date, time, doctor_id, user_id):
    date_index = int(date) - 1
    doctor = doctor_col.find_one({"doctor_id": doctor_id})
    slots = doctor["slots"]
    time_str = str(time)

    if slots[date_index][time_str] > 0:
        slots[date_index][time_str] -= 1
        doctor_col.update_one({"doctor_id": doctor_id}, {"$set": {"slots": slots}})

        appointment_time = "{:02d}:{:02d}".format(time, 10 * (5 - slots[date_index][time_str]))
        appointment_doc = {
            "date": date,
            "time": appointment_time,
            "doctor_id": doctor_id,
            "user_id": user_id
        }
        result = appointment_col.insert_one(appointment_doc)
        appointment_col.update_one({"_id": result.inserted_id}, {"$set": {"appointment_id": str(result.inserted_id)}})

        # Update user history
        user = user_col.find_one({"user_id": user_id})
        history = user.get("appointment_history", [])
        history.append(str(result.inserted_id))
        user_col.update_one({"user_id": user_id}, {"$set": {"appointment_history": history}})

        return str(result.inserted_id)
    else:
        return "SLOT_NOT_AVAILABLE"

def getAppointmentDetails(appointment_id):
    appointment = appointment_col.find_one({"appointment_id": appointment_id})
    user = user_col.find_one({"user_id": appointment["user_id"]})
    doctor = doctor_col.find_one({"doctor_id": appointment["doctor_id"]})

    return {
        "user_name": user["name"],
        "doctor_name": doctor["name"],
        "date": appointment["date"],
        "time": appointment["time"]
    }

def getHistory(user_id):
    user = user_col.find_one({"user_id": user_id})
    history_ids = user.get("appointment_history", [])
    return [getAppointmentDetails(appointment_id) for appointment_id in history_ids]





