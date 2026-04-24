from rest_framework import mixins, status
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from app.product.models import Category, ModelProduct, Product
from app.product.serializers import (
    ModelProductSerializer, ProductCreateSerializer, ProductDetailSerializer,
    ProductSerializer, CategorySerializer
)
from app.custom_pagination import CustomPagination
from app.custom_filters import ProductFilter

class ProductViewSet(
    mixins.ListModelMixin, - 
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


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

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ModelProductViewSet(viewsets.ModelViewSet):
    queryset = ModelProduct.objects.all()
    serializer_class = ModelProductSerializer