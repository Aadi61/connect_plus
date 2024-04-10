from . import db

carpool_collection = "carpool"

def add_carpool_details(name, contact_no, time, destination):
    carpool_ref = db.collection(carpool_collection).document()
    carpool_ref.set({
        "name": name,
        "contact_no": contact_no,
        "time": time,
        "destination": destination
    })
    carpool_id = carpool_ref.id
    carpool_ref.update({"carpool_id": carpool_id})
    return carpool_id

def retrieveList(timeSlot, destination):
    startTime = int(timeSlot[0:2])
    endTime = int(timeSlot[2:4])
    carpool_documents = db.collection(carpool_collection).get()
    carpool_matches = []
    for carpool_document in carpool_documents:
        carpool_dict = carpool_document.to_dict()
        if (carpool_dict['time'] >= startTime and carpool_dict['time'] <= endTime and carpool_dict['destination'] == destination):
            carpool_matches.append(carpool_dict)
    return carpool_matches
