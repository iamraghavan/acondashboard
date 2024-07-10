# firebase_service.py
import pyrebase
from django.conf import settings

firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)
storage = firebase.storage()

def upload_image(folder_id, image):
    bucket = storage.bucket()
    image_path = 'folders/' + folder_id + '/' + image.name
    blob = bucket.blob(image_path)
    blob.upload_from_string(image.read(), content_type=image.content_type)
    return blob.public_url

def delete_image(image_url):
    bucket = storage.bucket()
    blob = bucket.blob(image_url)
    blob.delete()