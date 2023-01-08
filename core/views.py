from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied

from django.conf import settings

from .serializers import UserSerializer

from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
User = get_user_model()

import jwt

class RegisterAPIView(APIView):
    def post(self, request):
        serialized_data = UserSerializer(data=request.data)

        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user_to_login = User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied("Invalid login details")
        
        if not user_to_login.check_password(password):
            raise PermissionDenied("Invalid login details")

        expiry_time = datetime.utcnow() + timedelta(hours=1)

        token = jwt.encode(
            {
                "id": str(user_to_login.id),
                "exp": expiry_time
            },
            settings.SECRET_KEY,
            "HS256"
        )

        return Response({"token": token})

