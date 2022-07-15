from django.contrib import admin

from blog.models import Article
from .models import Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Article)