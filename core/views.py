from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.validators import ValidationError

class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        if data["title"] == "Please select":
            # raise ValidationError({"message": "Select valid title"})
            return Response({"message": "select valid title"}, 
            status=status.HTTP_400_BAD_REQUEST)
        elif not data["first_name"].isalpha():
            raise ValidationError({"message": 
            "First name must be valid (only letters)"})
        elif not data["last_name"].isalpha():
            raise ValidationError({"message": 
            "Last name must be valid (only letters)"})
        elif "@" not in data["email"] or "." not in data["email"]:
            raise ValidationError({"message": 
            "Email address must be valid"})
        elif len(data["password"]) < 8:
            raise ValidationError({"message": 
            "Password must be 8 chars long"})
        elif data["password"] == data["password"].lower():
            raise ValidationError({"message": 
            "Password must contain at least one upper case letter"})
        elif not any(char.isdigit() for char in data["password"]):
            raise ValidationError({"message": 
            "Password must contain at least one number"})

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)