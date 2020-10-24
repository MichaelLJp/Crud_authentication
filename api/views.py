from django.shortcuts import render,redirect
from rest_framework import generics
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Persona, Libro
from .serializers import PersonaSerializer
from .forms import CustomUserForm, LibroForm

def inicio(request):
    return render(request,'base.html')

def listado_books(request):
    libros = Libro.objects.all()
    data = {
        'libros':libros
    }
    return render(request,'listado_libros.html',data)

def nuevo_book(request):
    data ={
        'form':LibroForm()
    }
    if request.method == 'POST':
        formulario = LibroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']= "Guardado correctamente"
  
    return render(request,'nuevo_libro.html',data) 

def editar_book(request, id):
    libro = Libro.objects.get(id=id)
    if request.method == 'GET':
        form = LibroForm(instance = libro) 
        data ={
            'form': form
        }
    else:
        form =LibroForm(request.POST, instance = libro)
        data = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('listado_libros')
    return render(request,'edit_libro.html',data) 

def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }
    

    if request.method =='POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autenticar al usuario
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect( to='login')


    return render(request,'registration/registrar.html',data)
class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('libro_list')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,*kwargs)

    def form_valid(self,form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user = user)
        if token:
            login(self.request, form.get_user())
            return super(Login,self).form_valid(form)

class Logout(APIView):
    def get(self,request, format = None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status = status.HTTP_200_OK)

