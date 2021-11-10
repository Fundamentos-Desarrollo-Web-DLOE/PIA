from django.db import models

# Create your models here.
class Sucursal (models.Model):
    nombre=models.CharField(max_length=50)
    NumerodeSucursal=models.FloatField()
    direccion=models.TextField()
    codigopostal=models.FloatField()


    def __str__(self):
        return self.nombre