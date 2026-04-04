from django.contrib import admin
from app.product.models import Category, ModelProduct, Product, ProductImage

# Register your models here.
admin.site.register(Category)
admin.site.register(ModelProduct)
admin.site.register(Product)
admin.site.register(ProductImage)