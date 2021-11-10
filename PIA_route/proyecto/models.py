from django.db import models

# Create your models here.
class Proyecto (models.Model):
    nombre=models.CharField(max_length=50)
    empresa=models.CharField(max_length=50)
    lenguaje=models.CharField(max_length=50)


    def __str__(self):
        return self.nombre