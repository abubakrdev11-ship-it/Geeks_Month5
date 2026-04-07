from rest_framework import mixins, generics
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

from app.user.models import User
from app.user.serializers import RegisterSerializer, TokenObtainPairSerializer, UserSerializer

class RegisterAPI(mixins.CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class CustomToken(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

class ProfileAPI(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    

