import imp
from django.urls import path
from carapp import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('getbrands', views.get_brands, name='getbrands'),
    path('getmodels', views.get_models, name='getmodels'),
    path('', views.get_price, name='getprice'),
]