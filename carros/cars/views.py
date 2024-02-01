from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    # cars = Car.objects.filter(brand=3)
    # cars = Car.objects.filter(brand__name='Chevrolet')
    # cars = Car.objects.filter(model='Chevette Tubarão')
    cars = Car.objects.filter(model__contains='Chevette')
    print(cars)
    
    
    
    return render(
        request,
        'cars.html',
        {'cars': cars}
        )