from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import UsuariosForm
from .models import Usuarios

# Create your views here.

def home(request):
    return render(request,'CRUD/home.html')

@login_required
def usuarioFormView(request):
    form = UsuariosForm()
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_url')
    template_name = 'CRUD/create.html'
    context = {'form': form,
               'boton':'Crear'}
    return render(request, template_name, context)

@login_required
def listaView(request):
    obj = Usuarios.objects.all()
    template_name = 'CRUD/lista.html'
    context = {'obj': obj}
    return render(request, template_name, context)

@login_required
def updateView(request, f_cedula):
    obj = Usuarios.objects.get(cedula=f_cedula)
    
    form = UsuariosForm(instance=obj)
    if request.method == 'POST':
        form = UsuariosForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            if f_cedula != form.cleaned_data['cedula']:
                objDelete = Usuarios.objects.get(cedula=f_cedula)
                objDelete.delete()
            
            return redirect('lista_url')
    
    template_name = 'CRUD/create.html'
    context = {'form': form,
                'boton':'Editar'}
    return render(request, template_name, context)

@login_required
def deleteView(request, f_cedula):
    obj = Usuarios.objects.get(cedula=f_cedula)
    if request.method == 'POST':
        obj.delete()
        return redirect('lista_url')
    template_name = 'CRUD/confirmation.html'
    context = {'obj': obj}
    return render(request, template_name, context)


def exit(request):
    logout(request)
    return redirect('home')

