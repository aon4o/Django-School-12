import requests
from django.http import JsonResponse
from django.shortcuts import render

from .models import Car
from .forms import LimitForms
from .serializers import CarSerializer


def index(request):
    form = LimitForms()
    limit = 10
    page = 0
    prev = ''
    next = ''
    
    if 'limit' in request.GET:
        limit = request.GET['limit']
        form = LimitForms({'limit': limit})

    link = 'https://api-v3.mbta.com/predictions?page%5Boffset%5D=' \
           f'0&page%5Blimit%5D={limit}&filter%5Bstop%5D=place-north'
    
    if 'page' in request.GET:
        link = request.GET['page']
    
    response = requests.get(link).json()
    
    if 'next' in response['links']:
        next = response['links']['next']
    if 'prev' in response['links']:
        prev = response['links']['prev']
    
    return render(request, "index.html", {'response': response['data'],
                                          'prev': prev,
                                          'next': next,
                                          'form': form})


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def cars(request):
    return render(request, 'cars.html')


def cars_json(request):
    cars = Car.objects.all()
    return JsonResponse(CarSerializer(cars, many=True).data, safe=False)


