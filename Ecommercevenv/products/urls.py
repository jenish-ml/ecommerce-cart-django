from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('products',views.products_list,name='products'),
    path('detail_product/<int:id>',views.detail_product,name='detail_product'),
    path('search/', views.products_list, name='search'),
    path('navbar', views.products_list, name='navbar'),
]