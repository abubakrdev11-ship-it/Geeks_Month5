from rest_framework.routers import DefaultRouter
from django.urls import path

from app.product.views import (
    ProductViewSet, CategoryViewSet, ModelProductViewSet
)

router = DefaultRouter()
router.register("product", ProductViewSet, basename='product')
router = DefaultRouter()
router.register("products", ProductViewSet, basename='products')
router.register("categories", CategoryViewSet, basename='categories')
router.register("models", ModelProductViewSet, basename='models')

urlpatterns = [
    
]

urlpatterns += router.urls
