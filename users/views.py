from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from users.forms import UserEditForm, UserRegisterForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Imagen

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contrasenia)
            
            if user is not None:
                login(request, user)
                return redirect("Inicio")  
            
        return render(request, "users/login.html", {"form": form, "msg_login": "Usuario o contraseña incorrectos"})
    
    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect("Inicio")  
        else:
            
            return render(request, "users/registro.html", {"form": form})
    
    form = UserRegisterForm()
    return render(request, "users/registro.html", {"form": form})


def editar_perfil(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)
        if miFormulario.is_valid():
            print(miFormulario.cleaned_data)
            miFormulario.save()
            if miFormulario.cleaned_data.get('imagen'):
                imagen, created = Imagen.objects.get_or_create(user=usuario)
                imagen.imagen = miFormulario.cleaned_data.get('imagen')
                imagen.save()
            return redirect("Inicio")  

    else:
        miFormulario = UserEditForm(instance=usuario)

    return render(request, "users/editar_usuario.html", {"mi_form": miFormulario, "usuario": usuario})

class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/editar_pass.html"
    success_url = reverse_lazy("EditarPerfil")
