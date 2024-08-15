from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import IngresarDatosForm
from .models import DatosAlmacenados
from django.contrib import messages

def inicio(request):
    return render(request, 'Proyecto/inicio.html', {'usuario_autenticado': request.user.is_authenticated})

def sobre_nosotros(request):
    return render(request, 'Proyecto/sobre_nosotros.html')

@login_required
def ingresar_datos(request):
    if request.method == 'POST':
        form = IngresarDatosForm(request.POST)
        if form.is_valid():
            datos = form.save(commit=False)
            datos.user = request.user
            datos.save()
            messages.success(request, 'Datos ingresados exitosamente.')
            return redirect('Ver Datos')  
    else:
        form = IngresarDatosForm()
    return render(request, 'Proyecto/ingresar_datos.html', {'form': form})

@login_required
def ver_datos_almacenados(request):
    datos_almacenados = DatosAlmacenados.objects.filter(user=request.user).order_by('-date')
    return render(request, 'Proyecto/ver_datos_almacenados.html', {'datos_almacenados': datos_almacenados})

class DatosAlmacenadosDelete(DeleteView):
    model = DatosAlmacenados
    success_url = reverse_lazy('Ver Datos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object
        return context