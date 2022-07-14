from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProductForm, RawProductForm
from .models import Product
# Create your views here.

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj,
    }
    return render(request, 'product/detail.html', context)


# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     # obj = Product.objects.get(id=1)
#     # context = {
#     #     'title': obj.title,
#     #     'description': obj.description,
#     #     }
#     context = {
#         'form': form,
#     }
#     return render(request, 'product/product_create_view.html', context)

# def product_create_view(request):
#     # print(request.POST)
#     # print(request.GET)
#     if request.method == 'POST':
#         new_title = request.POST.get('title')
#         print(new_title)
#     context = {}
#     return render(request, 'product/product_create_view.html', context)

def product_create_view(request):
    form = RawProductForm()
    context = {
        'form': form,
    }
    return render(request, 'product/product_create_view.html', context)