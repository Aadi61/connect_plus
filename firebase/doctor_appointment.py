from __init__ import db

doctor_collection = "doctor"
appointment_collection = "appointment"
user_collection = "user"

# Add doctor details to the database
def add_doctor_detail(name, venue, type, slots):
    doctor_ref = db.collection(doctor_collection).document()
    doctor_ref.set({
        "name": name,
        "venue": venue,
        "type": type,
        "slots": slots,
        "image_url":"https://www.shutterstock.com/image-photo/healthcare-medical-staff-concept-portrait-600nw-2281024823.jpg"
    })
    doctor_id = doctor_ref.id
    doctor_ref.update({"doctor_id": doctor_id})
    return doctor_id

# Add user details to the database
def add_user_detail(name, email, password, appointment_history):
    user_ref = db.collection(user_collection).document()
    user_ref.set({
        "name": name,
        "email": email,
        "password": password,
        "appointment_history": appointment_history
    })
    user_id = user_ref.id
    user_ref.update({"user_id": user_id})
    return user_id

# Retrieve doctor details of a particular doctor at a particular date
def retreiveTimeList(doctor_id, date):
    timingsInt = db.collection(doctor_collection).document(doctor_id).get().to_dict().get("slots")[date-1]
    timingsList = []
    for i in range(0, 24):
        j = str(i)
        if timingsInt[j] > 0:
            timingsList.append(i)
    return timingsList

# Retrieve doctor details of all doctors
def get_all_doctor_details():
    doctor_details = []
    doctors = db.collection(doctor_collection).get()
    for doctor in doctors:
        doctor_data = doctor.to_dict()
        doctor_details.append({
            "name": doctor_data["name"],
            "venue": doctor_data["venue"],
            "type": doctor_data["type"]
        })
    return doctor_details

# Book function
def book(date, time, doctor_id, user_id):
    date_time = db.collection(doctor_collection).document(doctor_id).get().to_dict().get("slots")
    timingsList = date_time[date-1]
    timeStr = str(time)
    if (timingsList[timeStr] > 0):
        timingsList[timeStr] -= 1
        db.collection(doctor_collection).document(doctor_id).update({"slots":date_time})
        appointmentTime = "{:02d}:{:02d}".format(time, 10*(5-timingsList[timeStr]))
        appointment_ref = db.collection(appointment_collection).document()
        appointment_ref.set({
            "date":date,
            "time":appointmentTime,
            "doctor_id":doctor_id,
            "user_id":user_id
        })
        appointment_id = appointment_ref.id
        appointment_ref.update({"appointment_id":appointment_id})
        history = db.collection(user_collection).document(user_id).get().to_dict().get("appointment_history")
        history.append(appointment_id)
        db.collection(user_collection).document(user_id).update({"appointment_history":history})
        return appointment_id
    else:
        return 0


#history function
def getHistory(user_id):
    history = db.collection(user_collection).document(user_id).get().to_dict().get("appointment_history")
    return history

add_doctor_detail("ABC", "AB1", "General", )