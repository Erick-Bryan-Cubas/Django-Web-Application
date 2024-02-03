from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all()
    search  = request.GET.get('search')
    if search:
        cars = Car.objects.filter(model__contains=search)
    
    # print(request) # Captura os parametros de query request do usuario
    # print(request.GET.get('search')) # Captura os valores da query request do usuario
    # cars = Car.objects.filter(brand=3)
    # cars = Car.objects.filter(brand__name='Chevrolet')
    # cars = Car.objects.filter(model='Chevette Tubarão')
    # cars = Car.objects.filter(model__contains='Chevette')
   
    return render(
        request,
        'cars.html',
        {'cars': cars}
        )