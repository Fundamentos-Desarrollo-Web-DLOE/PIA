from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sucursales(request):
    return render(request,'sucursales.html')

