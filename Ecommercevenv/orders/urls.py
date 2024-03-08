from . import views
from django.urls import path

urlpatterns = [
    path('cart',views.show_cart,name='cart'),
    path('orders',views.view_orders,name='orders'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('remove/<pk>',views.remove,name='remove'),
    path('checkout',views.checkout_cart,name='checkout'),
]