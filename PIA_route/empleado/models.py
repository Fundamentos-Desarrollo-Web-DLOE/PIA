from django.db import models

# Create your models here.
class Empleado (models.Model):
    matricula=models.FloatField(default=0)
    rfc=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    direccion=models.TextField()


    def __str__(self):
        return self.nombre