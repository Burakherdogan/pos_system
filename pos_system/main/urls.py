from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('reports', views.reports, name="reports"),
    path('', views.shopping_cart, name="shopping_cart"),
    path('add/', views.cart_add, name="cart_add"),
    path('delete', views.cart_delete, name="cart_delete"),
    path('update', views.cart_update, name="cart_update"),

]
