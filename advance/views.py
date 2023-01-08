from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from .models import Advance

from .serializers import AdvanceSerializer

class AdvanceListView(APIView):
    # permission_classes = (IsAuthenticated, )

    def post(self, request):
        advance_to_create = AdvanceSerializer(data=request.data)
        print(advance_to_create)
        print(request.user)

        if advance_to_create.is_valid(raise_exception=True):
            advance_to_create.save()
            return Response(advance_to_create.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def get(self, request):
        advances = Advance.objects.filter(user=self.request.id)

        print(advances)
