from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer

class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data

        serializer = UserSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)