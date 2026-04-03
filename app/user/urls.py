from rest_framework.routers import DefaultRouter
from django.urls import path
from app.user.views import CustomToken, ProfileAPI
from rest_framework_simplejwt.views import (
    TokenRefreshView, TokenBlacklistView
)

from app.user.views import RegisterAPI

router = DefaultRouter()
router.register("register", RegisterAPI, basename="register")

urlpatterns = [
    path("token/", CustomToken.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
    path("profile/", ProfileAPI.as_view(), name="profile"),
]

urlpatterns += router.urls
