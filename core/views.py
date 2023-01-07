# import datetime, random, string
# from rest_framework.views import APIView
# from rest_framework import exceptions
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import UserSerializer
# from rest_framework.validators import ValidationError
# from .models import User, UserToken, Reset
# from .authentication import (create_access_token, 
#     create_refresh_token,
#     JWTAuthentication,
#     decode_refresh_token)
# from django.core.mail import send_mail

# class RegisterAPIView(APIView):
#     def post(self, request):
#         data = request.data
#         serializer = UserSerializer(data=data)
#         serializer.is_valid(raise_exception=True)

#         if data["title"] == "Please select":
#             # raise ValidationError({"message": "Select valid title"})
#             return Response({"message": "select valid title"}, 
#             status=status.HTTP_400_BAD_REQUEST)
#         elif not data["first_name"].isalpha():
#             raise ValidationError({"message": 
#             "First name must be valid (only letters)"})
#         elif not data["last_name"].isalpha():
#             raise ValidationError({"message": 
#             "Last name must be valid (only letters)"})
#         elif "@" not in data["email"] or "." not in data["email"]:
#             raise ValidationError({"message": 
#             "Email address must be valid"})
#         elif len(data["password"]) < 8:
#             raise ValidationError({"message": 
#             "Password must be 8 chars long"})
#         elif data["password"] == data["password"].lower():
#             raise ValidationError({"message": 
#             "Password must contain at least one upper case letter"})
#         elif not any(char.isdigit() for char in data["password"]):
#             raise ValidationError({"message": 
#             "Password must contain at least one number"})

#         serializer.save()
#         print(serializer.data)
#         return Response(serializer.data)


# class LoginAPIView(APIView):
#     def post(self, request):
#         email = request.data["email"]
#         password = request.data["password"]

#         user = User.objects.filter(email=email).first()

#         if user is None:
#             raise exceptions.AuthenticationFailed("Invalid credentials")
        
#         if not user.check_password(password):
#             raise exceptions.AuthenticationFailed("Invalid credentials")
        
#         access_token = create_access_token(user.id.__str__())
#         refresh_token = create_refresh_token(user.id.__str__())
        
#         UserToken.objects.create(
#             user_id=user.id,
#             token=refresh_token,
#             expired_at=datetime.datetime.utcnow() + datetime.timedelta(days=7)
#         )

#         response = Response()

#         # response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
#         response.data = {
#             "access_token": access_token,
#             "refresh_token": refresh_token
#         }
#         print(response)
#         return response

# class UserAPIView(APIView):
#     authentication_classes = [JWTAuthentication]

#     def get(self, request):
#         return Response(UserSerializer(request.user).data)


# class RefreshAPIView(APIView):
#     def post(self, request):
#         refresh_token = request.data["refresh_token"]
#         id = decode_refresh_token(refresh_token)

#         if not UserToken.objects.filter(
#             user_id=id,
#             token=refresh_token,
#             expired_at__gt=datetime.datetime.now(tz=datetime.timezone.utc)
#         ).exists():
#             raise exceptions.AuthenticationFailed("unathenticated")

#         access_token = create_access_token(id)

#         return Response({
#             "access_token": access_token
#         })


# class LogoutAPIView(APIView):
#     def post(self, request):
#         refresh_token = request.COOKIES.get("refresh_token")

#         UserToken.objects.filter(token=refresh_token).delete()

#         response = Response()
#         response.delete_cookie(key="refresh_token")
#         response.data = {
#             "message": "success"
#         }

#         return response


# class ForgotAPIView(APIView):
#     def post(self, request):
#         email = request.data["email"]
#         token = ''.join(random.choice(string.ascii_lowercase 
#             + string.digits) for _ in range(10))
        
#         Reset.objects.create(
#             email=email,
#             token=token
#         )

#         url = 'http://localhost:3000/reset/' + token

#         send_mail(
#             subject="Reset your password",
#             message="Click %s to reset password" %url,
#             from_email="example@example.com",
#             recipient_list=[email]
#         )

#         return Response({
#             "message": "success"
#         })
    

# class ResetAPIView(APIView):
#     def post(self, request):
#         data = request.data

#         reset_password = Reset.objects.filter(token=data["token"].first())
    
#         if not reset_password:
#             raise exceptions.APIException("Invalid link!")
        
#         user = User.objects.filter(email=reset_password.email).first()

#         if not user:
#             raise exceptions.APIException("User not found!")
        
#         user.set_password(data["password"])
#         user.save()

#         return Response({
#             "message": "success"
#         }) 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer

from django.contrib.auth import get_user_model

class RegisterAPIView(APIView):
    def post(self, request):
        serialized_data = UserSerializer(data=request.data)

        try:
            serialized_data.is_valid()
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_202_ACCEPTED)
        except Exception as e: 
            print(e)
            return Response(e.__dict__ if e.__dict__ else str(e),
            status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        # print(request.data)