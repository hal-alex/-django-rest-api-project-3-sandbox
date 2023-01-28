from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from .serializers import AdvSerializer
from .models import Adv

class AdvListView(APIView):
    # authentication_classes = (authentication.TokenAuthentication)
    def post(self, request):
        print("REQUEST ID", request.user)
        adv_to_create = AdvSerializer(data=request.data)

        try:
            adv_to_create.is_valid(raise_exception=True) 
            adv_to_create.save() 
            return Response(adv_to_create.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)

