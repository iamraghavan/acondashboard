import os
import firebase_admin
from firebase_admin import credentials, storage

# Path to your Firebase admin SDK JSON file
FIREBASE_ADMIN_SDK_PATH = os.path.join(os.path.dirname(__file__), 'static', 'andavarcon-firebase-adminsdk.json')

# Initialize the Firebase app only if it hasn't been initialized yet
if not firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_ADMIN_SDK_PATH)
    firebase_admin.initialize_app(cred, {'storageBucket': 'andavarcon.appspot.com'})

# Get a reference to the storage client
storage_client = storage.bucket()
