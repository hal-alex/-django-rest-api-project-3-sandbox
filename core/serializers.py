from rest_framework.serializers import ModelSerializer
from .models import User
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        title = data["title"]
        first_name = data["first_name"]
        last_name = data["last_name"]
        email_address = data["email"]
        password = data["password"]
        if title == "Please select":
            raise ValidationError({"title": "Select valid title"})
        elif not first_name.isalpha():
            raise ValidationError({"first_name": 
            "First name must be valid (only letters)"})
        elif not last_name.isalpha():
            raise ValidationError({"last_name": 
            "Last name must be valid (only letters)"})
        elif "@" not in email_address or "." not in email_address:
            raise ValidationError({"email_address": 
            "Email address must be valid"})
        elif len(password) < 8:
            raise ValidationError({"password": 
            "Password must be 8 chars long"})
        elif password == password.lower():
            raise ValidationError({"password": 
            "Password must contain at least one upper case letter"})
        elif not any(char.isdigit() for char in password):
            raise ValidationError({"password": 
            "Password must contain at least one number"})
        
        password = make_password(password)
        
        return data

    class Meta:
        model = User
        fields = ["id", "email", "title", "first_name", "last_name", "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }
        
    # def create(self, validated_data):
    #     password = validated_data.pop("password", None)
    #     instance = self.Meta.model(**validated_data)

    #     if password is not None: 
    #         instance.set_password(password)

    #     instance.save()

    #     return instance


