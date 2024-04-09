import firebase_admin
from firebase_admin import credentials, firestore, storage

cred = credentials.Certificate("./credentials.json")
firebase_admin.initialize_app(cred, {'storageBucket': 'connectplus-49390.appspot.com'})


db = firestore.client()
bucket = storage.bucket('connectplus-49390.appspot.com')



