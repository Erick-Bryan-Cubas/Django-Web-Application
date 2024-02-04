from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm

def cars_view(request):
    cars = Car.objects.all().order_by('model')
    # cars = Car.objects.all().order_by('-model') # Ordenação invertida
    search  = request.GET.get('search')
    if search:
        # cars = Car.objects.filter(model__contains=search)
        cars = Car.objects.filter(model__icontains=search) # ignore case
        # cars = Car.objects.filter(model__icontains=search).order_by('model') # Ordenação dos dados
        
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
    
def new_car_view(request):
    if request.method =='POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')        
        # print(new_car_form.data) # Captura dos dados formulados
    else:      
        new_car_form = CarModelForm()
    return render(request, 'new_car.html', {'new_car_form': new_car_form})