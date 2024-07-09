import jwt
from django.http import JsonResponse
from django.conf import settings

class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/dashboard'):
            token = request.META.get('HTTP_AUTHORIZATION')
            if not token:
                return JsonResponse({"error": "Unauthorized access"}, status=401)

            try:
                decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                request.user_id = decoded['user_id']
            except jwt.ExpiredSignatureError:
                return JsonResponse({"error": "Token expired"}, status=401)
            except jwt.InvalidTokenError:
                return JsonResponse({"error": "Invalid token"}, status=401)

        response = self.get_response(request)
        return response
