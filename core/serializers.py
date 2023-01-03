from rest_framework.serializers import ModelSerializer
from .models import User
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import ValidationError

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "title", "first_name", "last_name", "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }
    
    # def validate(self, request):
    #     title = request["title"]
    #     if title == "Please select":
    #         raise ValidationError("Select valid title")
    
    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)

        if password is not None: 
            isinstance.set_password(password)

        instance.save()

        return instance


