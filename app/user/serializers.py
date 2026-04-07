from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as SimpleJWTTokenObtainPairSerializer
from app.user.models import  User

class RegisterSerializer(serializers.ModelSerializer): 
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id", "email", "first_name", "last_name",
            "password"
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "created_at"]
        read_only_fields = ["id", "email", "created_at"]


class TokenObtainPairSerializer(SimpleJWTTokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data["user_id"] = self.user.id
        data["email"] = self.user.email
        return data