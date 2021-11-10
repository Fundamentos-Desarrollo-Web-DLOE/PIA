from django.db import models

# Create your models here.
class Cliente (models.Model):
    rfc=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    edad=models.FloatField()


    def __str__(self):
        return self.nombre