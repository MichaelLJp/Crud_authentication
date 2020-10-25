from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserForm

def nuevo_user(request):
    data ={
        'form': CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']= "Guardado correctamente"
            return redirect('list_users')

    return render(request,'nuevo_user.html',data) 

def editar_user(request,id):
    libro = User.objects.get(id=id)
    data = {
            'form':CustomUserForm(instance=libro)
        }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST, instance =libro)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']= "Guardado correctamente"
            data['form']=formulario
            return redirect('list_users')
    return render(request,'users/edit_user.html',data) 

def eliminar_user(request,id):
    libro = User.objects.get(id = id)
    libro.delete()
    return redirect('list_users')
    return render(request,'eliminar_user.html')