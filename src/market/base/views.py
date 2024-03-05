from django.shortcuts import render
from market.product.models import City, Category, Product, ProductImage
from django.db.models import Prefetch, Subquery, OuterRef
from market.user.models import User


# Django ORM - Object Relational Mapper   ==>   DATABASEdan  ma'lumotlarni  olib  kelish
def index(request):
    cities = City.objects.all()
    categories = Category.objects.all()

    context = {
        "cities": cities,
        "categories": categories
    }
    return render(request, 'index.html', context)


def category(request):
    custom_word = request.GET.get('customword', None)
    city = request.GET.get('city', None)
    category = request.GET.get('category', None)

    city = int(city) if city and city.isdigit() else None
    category = int(category) if category and category.isdigit() else None

    cities = City.objects.all()
    categories = Category.objects.all()

    if city and category:
        products = Product.objects.filter(city_id=city).filter(category_id=category).select_related('category', 'user', 'city').prefetch_related(
            Prefetch('productimage_set', queryset=ProductImage.objects.all())
        ).annotate(
            parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name'))
        )
    else:
        products = Product.objects.select_related('category', 'user', 'city').prefetch_related(
            Prefetch('productimage_set', queryset=ProductImage.objects.all())
        ).annotate(
            parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name'))
        )
    _format_products = []
    for i in products:
        _format_products.append({
            'id': i.id,
            "title": i.title,
            "description": i.description,
            "price": i.price,
            'user': i.user.username,
            "city": i.city.name,
            "category": i.category.name,
            "parent_category": i.parent_category_name,
            'discount': i.discount,
            # 'image': i.productimage_set.all()[0].image
        })
        # print(product.title, product.category.name, product.user.username, product.city.name)
        # print(product.parent_category_name)
        # print(product.productimage_set.all())

    context = {
        "cities": cities,
        "categories": categories,
        "products": _format_products,
        "selected_city": city,
        "select_ctg": category
    }
    return render(request, 'category.html', context)
