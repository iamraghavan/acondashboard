import jwt
from datetime import datetime, timedelta


def create_jwt_token(uid):
    payload = {
        "uid": uid,
        "exp": datetime.utcnow() + timedelta(days=1),
        "iat": datetime.utcnow()
    }
    token = jwt.encode(payload, "49tooAZhC7vGqHM2PJ5VKYy4vi5TNXqU", algorithm="HS256")
    return token
