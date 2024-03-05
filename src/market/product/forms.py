from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'city', 'price', 'discount', 'condition', 'address']
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control input-md", "placeholder": "Title"}),
            "category": forms.Select(attrs={"class": "tg-select form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control input-md", "placeholder": "Ad your Price"}),
            "discount": forms.NumberInput(attrs={"class": "form-control input-md", "placeholder": "Ad your discount"}),
            "city": forms.Select(attrs={"class": "tg-select form-control"}),
            "condition": forms.Select(attrs={"class": "tg-select form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control input-md"}),
        }


class ProductImageForm(forms.Form):
    image = forms.ImageField(label='image')


ProductImageFormSet = forms.formset_factory(ProductImageForm, extra=2)

