from django.urls import include, path
from api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('cars', views.cars, name='cars'),
    path('api/v1/cars', views.cars_json, name='cars_json'),
]
