from django.contrib import admin
from .models import Category, City, Product, ProductImage

admin.site.register(Category)
admin.site.register(City)
admin.site.register(Product)
admin.site.register(ProductImage)
