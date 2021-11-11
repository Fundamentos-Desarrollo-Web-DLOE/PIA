from django.db import models

# Create your models here.
class Empleado (models.Model):
    matricula=models.FloatField(default=0)
    rfc=models.CharField(max_length=50,default="")
    nombre=models.CharField(max_length=50,default="")
    apellido_Paterno=models.CharField(max_length=50,default="")
    apellido_Materno=models.CharField(max_length=50,default="")
    direccion=models.TextField()


    def __str__(self):
        return str(self.matricula)+"-"+self.nombre