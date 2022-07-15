"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from pages.views import home_view, contact_view, about_view
from web.views import product_detail_view, product_create_view, render_initial_data, dynamic_lookup_view, product_delete_view, product_list_view, product_update_view


urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('web/', include('web.urls')),
    path('', home_view, name='home'),
    path('about/', about_view),
    path('contact/', contact_view),
    path('product/', product_detail_view),
    path('create/', product_create_view),
    path('product/<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('product/<int:id>/delete/', product_delete_view, name='product-delete'),
    path('product/update/<int:id>/', product_update_view, name='product-update'),
    path('products/', product_list_view, name='products-list'),
]
