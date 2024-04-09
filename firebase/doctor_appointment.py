from . import db

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
        "slots": slots
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
        if timingsInt[i] > 0:
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

#Add appointment details to the database
# def add_appointment_detail(doctor_id, user_id, slots):
#     appointment_ref = db.collection(appointment_collection).document()
#     appointment_ref.set({
#         "doctor_id": doctor_id,
#         "user_id": user_id,
#         "slots": slots
#     })
#     appointment_id = appointment_ref.id
#     appointment_ref.update({"appointment_id": appointment_id})
#     return appointment_id

# Book function
def book(date, time, doctor_id, user_id):
    date_time = db.collection(doctor_collection).document(doctor_id).get().to_dict().get("slots")
    timingsList = date_time[date-1]
    if (timingsList[time] > 0):
        timingsList[time] -= 1
        db.collection(doctor_collection).document(doctor_id).update({"slots":date_time})
        appointmentTime = "{:02d}:{:02d}".format(time, 10*(5-timingsList[time]))
        appointment_ref = db.collection(appointment_ref).document()
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


d_id = add_doctor_detail("Dr. A", "Venue A", "General", [[0,0,0,6,6], [6,0,0,0,6],[6,6,6,6,6],[6,6,6,6,6],[6,6,6,0,6]])
u_id = add_user_detail("User A", "aa@gmail.com", "1234", [])
book(1, 3, d_id, u_id)