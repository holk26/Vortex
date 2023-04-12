from django.db import models

# Create your models here.

class Driver(models.Model):
    identificacion = models.CharField(max_length=20, null=False)
    apellido = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20, null=False)
    telefono = models.CharField(max_length=10, null=False)
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+' '+self.apellido
    
    def get_available_drivers(self):
        return Driver.objects.exclude(id=self.conductor_id)

    def associate_driver(self, driver_id):
        driver = Driver.objects.get(id=driver_id)
        self.conductor = driver
        self.save()

    def disassociate_driver(self):
        self.conductor = None
        self.save()


class Order(models.Model):
    tipo_pedido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50, null=False)
    conductor = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_pedido


class Vehicle(models.Model):
    modelo = models.CharField(max_length=4, null=False)
    placa = models.CharField(max_length=7, null=False)
    capacidad = models.CharField(max_length=7)
    conductor = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.modelo+' - '+self.placa