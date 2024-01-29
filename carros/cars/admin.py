from django.contrib import admin
from cars.models import Car

class CarAdmin(admin.ModelAdmin):
    """
    Administração personalizada para o modelo Car.

    Atributos:
        list_display (tuple): Campos a serem exibidos na lista de carros no painel de administração.
        search_fields (tuple): Campos pelos quais é possível pesquisar carros no painel de administração.

    Args:
        admin.ModelAdmin: Classe base para administração personalizada no Django.
    """
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'plate', 'value', 'photo')
    search_fields = ('model',)
    
admin.site.register(Car, CarAdmin)
