from django.shortcuts import render
from .forms import ProductForm, ProductImageFormSet


def product_create(request):
    form = ProductForm()
    if request.POST:
        form = ProductForm(request.POST or None)
        # formset = ProductImageFormSet()
        if form.is_valid():
            form.save()
    context = {
        "form": form,
        # "formset": formset,
    }
    return render(request, 'create.html', context)
