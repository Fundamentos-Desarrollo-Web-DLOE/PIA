from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cliente(request):
    return render(request,'cliente.html')

