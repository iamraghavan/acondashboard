import jwt
from datetime import datetime, timedelta

from django.contrib import messages
from firebase_admin import storage

def create_jwt_token(uid):
    payload = {
        "uid": uid,
        "exp": datetime.utcnow() + timedelta(days=1),
        "iat": datetime.utcnow()
    }
    token = jwt.encode(payload, "49tooAZhC7vGqHM2PJ5VKYy4vi5TNXqU", algorithm="HS256")
    return token


def validate_and_upload_image(image_file):
    if not image_file:
        raise ValueError("No image file provided.")
    if not image_file.name.lower().endswith('.webp'):
        raise ValueError("Please upload a .webp file.")
    if image_file.size > 2 * 1024 * 1024:  # 2MB limit
        raise ValueError("File size exceeds 2MB limit.")

    # Upload image to Firebase Storage
    image_path = f'event_images/{uuid.uuid4()}/{image_file.name}'
    storage.child(image_path).put(image_file)
    return storage.child(image_path).get_url(None)

def handle_firebase_exception(exception):
    messages.error(request, f"Error interacting with Firebase: {str(exception)}")
    return JsonResponse({'error': 'Firebase operation failed.'}, status=400)
