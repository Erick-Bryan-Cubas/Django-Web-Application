from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
 
    def __str__(self):
        return self.name
    
class Car(models.Model):
    """
    Representa um modelo de carro no sistema.

    Atributos:
        id (AutoField): Identificador único do carro (chave primária).
        model (CharField): Modelo do carro (até 200 caracteres).
        brand (ForeignKey): Marca do carro, chave estrangeira da tabela Brand
        factory_year (IntegerField): Ano de fabricação do carro (opcional).
        model_year (IntegerField): Ano do modelo do carro (opcional).
        plate(CharField): Plava do veículo (opcional).
        value (FloatField): Valor do carro (opcional).

    Observações:
        - Os campos factory_year, model_year e value são opcionais, podendo ser nulos.
    """
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/',blank=True, null=True)
    
    def __str__(self):
        return self.model
    
class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f'{self.cars_count} carros no valor total de R$ {self.cars_value:.2f	}'