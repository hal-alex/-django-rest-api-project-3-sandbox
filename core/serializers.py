from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }
    
    def create(self, validated_data):
        password = validated_data.pop("password", None)
        isinstance = self.Meta.model(**validated_data)
        if password is not None: 
            isinstance.set_password(password)
        isinstance.save()
        return isinstance
