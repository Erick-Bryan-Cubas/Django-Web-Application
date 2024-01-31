from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    cars = "hello"
    #cars = Car.objects.filter(brand=0)
    print(cars)
    
    
    
    return render(
        request,
        'cars.html',
        {'cars': cars}
        )