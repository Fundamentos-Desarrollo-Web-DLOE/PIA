from django.db import models

# Create your models here.
class Cliente (models.Model):
    matricula=models.FloatField(default=0)
    nombre=models.CharField(max_length=50,default="")
    apellidoPaterno=models.CharField(max_length=50,default="")
    apellidoMaterno=models.CharField(max_length=50,default="")
    edad=models.FloatField(default=0)

    

    def __str__(self):
        
        return str(self.matricula)