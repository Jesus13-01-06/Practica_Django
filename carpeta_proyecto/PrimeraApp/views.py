from django.shortcuts import render
from .models import animal, protectora, Colaborador

def animales(request):
    animales = animal.objects.all()  # obtiene todos los registros de animales
    return render(request, 'PrimeraApp/animal.html', {'animales': animales})

def protectoras(request):
    protectorass = protectora.objects.all()
    return render(request, 'PrimeraApp/protectora.html', {'protectoras': protectorass})

def colaboradores(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'PrimeraApp/Colaborador.html', {'colaboradores': colaboradores})
