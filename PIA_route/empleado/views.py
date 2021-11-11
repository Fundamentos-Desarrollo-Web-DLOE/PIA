from django.shortcuts import render
from django.http import HttpResponse
from .models import Empleado

# Create your views here.

def empleado(request):
    context={
        "data":Empleado.objects.all()
    }
    return render(request,'empleado.html',context)

