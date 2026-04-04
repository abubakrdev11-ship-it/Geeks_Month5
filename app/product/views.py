from rest_framework import mixins, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from app.product.models import Product
from app.product.serializers import (
    ProductCreateSerializer, ProductDetailSerializer,
    ProductSerializer
)

class ProductViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    
    def get_queryset(self):
        return (
            Product.objects.select_related("category", "model")
            .prefetch_related("product_image")
            .order_by("-created_at")
        )
    
    def get_serializer_class(self):
        if self.action == "create":
            return ProductCreateSerializer
        elif self.action == "retrieve":
            return ProductDetailSerializer
        return ProductSerializer

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated()]
        elif self.action == "retrieve":
            return [IsAuthenticated()]
        return [AllowAny()]
