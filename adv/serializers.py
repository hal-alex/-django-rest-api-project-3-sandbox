from rest_framework import serializers
from .models import Adv
from core.serializers import UserSerializer

class AdvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adv
        fields = ["description"]
        owner_id = UserSerializer()