from rest_framework.routers import DefaultRouter
from django.urls import path

from app.product.views import (
    ProductViewSet
)

router = DefaultRouter()
router.register("product", ProductViewSet, basename='product')

urlpatterns = [
    
]

urlpatterns += router.urls
