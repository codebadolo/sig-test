from django.shortcuts import render, redirect, get_object_or_404
from .models import Eleve
from .forms import EleveForm

def eleve_list(request):
    eleves = Eleve.objects.all()
    return render(request, 'eleve_list.html', {'eleves': eleves})

def eleve_detail(request, pk):
    eleve = get_object_or_404(Eleve, pk=pk)
    return render(request, 'eleve_detail.html', {'eleve': eleve})

def eleve_create(request):
    if request.method == 'POST':
        form = EleveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eleve_list')
    else:
        form = EleveForm()
    return render(request, 'eleve_form.html', {'form': form})

def eleve_update(request, pk):
    eleve = get_object_or_404(Eleve, pk=pk)
    if request.method == 'POST':
        form = EleveForm(request.POST, instance=eleve)
        if form.is_valid():
            form.save()
            return redirect('eleve_list')
    else:
        form = EleveForm(instance=eleve)
    return render(request, 'eleve_form.html', {'form': form})

def eleve_delete(request, pk):
    eleve = get_object_or_404(Eleve, pk=pk)
    if request.method == 'POST':
        eleve.delete()
        return redirect('eleve_list')
    return render(request, 'eleve_confirm_delete.html', {'eleve': eleve})

