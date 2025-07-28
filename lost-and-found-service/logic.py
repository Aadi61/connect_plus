import boto3
from botocore.exceptions import NoCredentialsError
from werkzeug.utils import secure_filename
import os
import uuid
from db import db

found_col = db["found"]
lost_col = db["lost"]

UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

S3_BUCKET = 'vit--connectplus'
S3_REGION = 'ap-south-1'
AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')

def upload_to_s3(file):
    filename = f"{uuid.uuid4()}_{secure_filename(file.filename)}"
    s3 = boto3.client('s3',
                      region_name=S3_REGION,
                      aws_access_key_id=AWS_ACCESS_KEY,
                      aws_secret_access_key=AWS_SECRET_KEY)
    try:
        s3.upload_fileobj(file, S3_BUCKET, filename, ExtraArgs={'ACL': 'public-read'})
        url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{filename}"
        return url
    except NoCredentialsError:
        return None


def add_found_item(name, image_url, place, contact, user_id, date_found):
    doc = {
        "name": name,
        "image_url": image_url,
        "place": place,
        "contact": contact,
        "user_id": user_id,
        "date_found": date_found,
        "returned": False
    }
    result = found_col.insert_one(doc)
    found_col.update_one({"_id": result.inserted_id}, {"$set": {"found_id": str(result.inserted_id)}})


def retreive_found_item(user_id):
    return list(found_col.find({"user_id": user_id}, {"_id": 0}))


def retreive_all_found_items():
    return list(found_col.find({}, {"_id": 0}))


def delete_found_item(found_id):
    found_col.delete_one({"found_id": found_id})


def add_lost_item(name, image_url, place, contact, user_id, date_lost):
    doc = {
        "name": name,
        "image_url": image_url,
        "place": place,
        "contact": contact,
        "user_id": user_id,
        "date_lost": date_lost
    }
    result = lost_col.insert_one(doc)
    lost_col.update_one({"_id": result.inserted_id}, {"$set": {"lost_id": str(result.inserted_id)}})
    return str(result.inserted_id)


def retreive_all_lost_items():
    return list(lost_col.find({}, {"_id": 0}))


def retrieve_lost_item(user_id):
    return list(lost_col.find({"user_id": user_id}, {"_id": 0}))


def mark_item_as_returned2(found_id):
    result = found_col.update_one({"found_id": found_id}, {"$set": {"returned": True}})
    return result.modified_count > 0
