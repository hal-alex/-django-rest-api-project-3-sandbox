from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data

        if len(data["password"]) < 8:
            raise exceptions.APIException("Password must be 8 chars long")

        serializer = UserSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(status=status.HTTP_201_CREATED)