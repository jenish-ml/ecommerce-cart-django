from . import views
from django.urls import path

urlpatterns = [
    path('account',views.show_account,name='account'),
    path('signout',views.signout,name='signout'),
]