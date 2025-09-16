from django.shortcuts import render, redirect, get_object_or_404
from .models import Ciudad
from .forms import CiudadForm
from pais.models import Pais

def listar_ciudades(request):
    ciudades = Ciudad.objects.filter(deleted=False)
    return render(request, 'ciudad/listar.html', {'ciudades': ciudades})

def ciudades_por_pais(request, pais_id):
    pais = get_object_or_404(Pais, id=pais_id)
    ciudades = Ciudad.objects.filter(pais=pais, deleted=False)
    return render(request, 'ciudad/listar.html', {
        'ciudades': ciudades,
        'pais': pais
    })

def crear_ciudad(request):
    if request.method == 'POST':
        form = CiudadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ciudad:listar')
    else:
        form = CiudadForm()
    return render(request, 'ciudad/formulario.html', {'form': form})

def editar_ciudad(request, id):
    ciudad = get_object_or_404(Ciudad, id=id)
    if request.method == 'POST':
        form = CiudadForm(request.POST, instance=ciudad)
        if form.is_valid():
            form.save()
            return redirect('ciudad:listar')
    else:
        form = CiudadForm(instance=ciudad)
    return render(request, 'ciudad/formulario.html', {'form': form})

def eliminar_ciudad(request, id):
    ciudad = get_object_or_404(Ciudad, id=id, deleted=False)
    if request.method == 'POST':
        ciudad.delete()
        return redirect('ciudad:listar')
    return render(request, 'ciudad/eliminar.html', {'ciudad': ciudad})

def restaurar_ciudad(request, id):
    ciudad = get_object_or_404(Ciudad, id=id, deleted=True)
    if request.method == 'POST':
        ciudad.restore()
        return redirect('ciudad:listar')
    return render(request, 'ciudad/restaurar.html', {'ciudad': ciudad})