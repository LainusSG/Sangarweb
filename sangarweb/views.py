
from django.shortcuts import render


def home_view(request):
    return render(request, 'base.html') 
 
def logo(request):
    return render(request, "sangartech.html")

def servicios(request):
    return render(request, "servicios.html")

def nosotros(request):
    return render(request, "nosotros.html")

def contacto(request):
    return render(request, "contacto.html")

def productos(request):
    return render(request, "productos.html")
