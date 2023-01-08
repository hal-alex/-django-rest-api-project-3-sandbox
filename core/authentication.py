# import jwt
# from datetime import datetime, timedelta
# from rest_framework import exceptions
# from rest_framework.authentication import BaseAuthentication, get_authorization_header
# from .models import User



# def create_access_token(id):
#     return jwt.encode({
#         "user_id": id,
#         "exp": datetime.now() + timedelta(seconds=30),
#         "iat": datetime.now()
#     }, "access_secret", algorithm="HS256")

# def decode_access_token(token):
#     try:
#         payload = jwt.decode(token, "access_secret", algorithms="HS256")

#         return payload["user_id"]
#     except:
#         raise exceptions.AuthenticationFailed("unathenticated")

# def create_refresh_token(id):
#     dt = datetime.now() + timedelta(days=7)

#     return jwt.encode({
#         "user_id": id,
#         "exp": int(dt.strftime('%S')),
#         "iat": datetime.now(),
#     }, "refresh_secret", algorithm="HS256")

# def decode_refresh_token(token):
#     try:
#         payload = jwt.decode(token, "refresh_secret", algorithms="HS256")

#         return payload["user_id"]
#     except:
#         raise exceptions.AuthenticationFailed("unathenticated")

# class JWTAuthentication(BaseAuthentication):
#     def authenticate(self, request):
#         auth = get_authorization_header(request).split()

#         if auth and len(auth) == 2:
#             token = auth[1].decode("utf-8")
#             id = decode_access_token(token)

#             user = User.objects.get(pk=id)

#             return (user, None)
        
#         raise exceptions.AuthenticationFailed("unathenticated")

from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt

User = get_user_model()


class JWTAuthentication(BasicAuthentication):

    def authenticate(self, request):
        header = request.headers["Authorization"]
        
        if not header:
            raise PermissionDenied("Auth header missing")
        
        if not header.startswith("Bearer"):
            raise PermissionDenied("Invalid token")
        
        token = header.replace("Bearer", "")

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, ["HS256"])
            user = User.objects.get(id=payload.get("id"))
        except jwt.exceptions.InvalidTokenError:
            raise PermissionDenied("Invalid token")
        except User.DoesNotExist:
            raise PermissionDenied("User not found")
        
        return (user, token)

        