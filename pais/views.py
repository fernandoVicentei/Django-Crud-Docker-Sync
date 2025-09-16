from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from .models import Pais
from .forms import PaisForm
from ciudad.models import Ciudad

def listar_paises(request):
    paises = Pais.objects.filter(deleted=False)
    return render(request, 'pais/listar.html', {'paises': paises})

def crear_pais(request):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pais:listar')
    else:
        form = PaisForm()
    return render(request, 'pais/formulario.html', {'form': form})

def editar_pais(request, id):
    pais = get_object_or_404(Pais, id=id)
    if request.method == 'POST':
        form = PaisForm(request.POST, instance=pais)
        if form.is_valid():
            form.save()
            return redirect('pais:listar')
    else:
        form = PaisForm(instance=pais)
    return render(request, 'pais/formulario.html', {'form': form})

def eliminar_pais(request, id):
    pais = get_object_or_404(Pais, id=id, deleted=False)
    if request.method == 'POST':
        pais.delete()
        return redirect('pais:listar')
    
    return render(request, 'pais/eliminar.html', {'pais': pais})


def listado_integrado(request):
    paises = Pais.objects.filter(deleted=False).prefetch_related(
        models.Prefetch(
                'ciudad_set',
                queryset=Ciudad.objects.filter(deleted=False, isActive=True),
            to_attr='ciudades_activas'
        )
    )
    
    return render(request, 'pais/listado_integrado.html', {
        'paises': paises
    })