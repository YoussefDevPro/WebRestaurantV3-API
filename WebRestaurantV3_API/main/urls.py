from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('menu/', views.menu, name="menu"),
    path('menu/pizza/', views.pizza, name="pizza"),
    path('menu/tacos/', views.tacos, name="tacos"),
    path('menu/burger/', views.burger, name="burger"),
    path('menu/plat/', views.plat, name="plat"),
    path('menu/sandwich/', views.sandwich, name="sandwich"),
    path('menu/dessert/', views.dessert, name="dessert"),
    path('order/', views.order_view, name='order'),
    path('reserver/', views.reserve_view, name='reserve'),
    path('API/IRVRVHNOIUNOUZHNOZIJNC/Get-All-Json-Data', views.api_get_all_json_data, name='API'),
]
