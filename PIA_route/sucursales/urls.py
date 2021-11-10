from django.urls import path
from . import views


urlpatterns = [
    path("sucursales/",views.sucursales,name="sucursales"),
]