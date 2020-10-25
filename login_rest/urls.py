"""login_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from api.views import Login,Logout,inicio,registro_usuario, listado_books,nuevo_book,editar_book,eliminar_book,listado_usuarios
from api.views_users import nuevo_user,editar_user,eliminar_user
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name='base'),
    path('api/1.0', include(('api.urls','api'))),
    path('api_generate_token/', views.obtain_auth_token),
    path('login/',Login.as_view(), name = 'login'),  
    path('logout/', Logout.as_view(),name ='logout'),
    path('api_generate_token/', views.obtain_auth_token),
    path('registro/',registro_usuario, name='registro_usuario'),
    path('listar-libro/',listado_books,name='libro_list'),
    path('nuevo-libro/',nuevo_book,name='libro_crear'),
    path('editar-libro/<id>/', editar_book, name= "editar_libro"),
    path('eliminar-libro/<id>/',eliminar_book, name = 'eliminar_libro'),

    path('listar-user/',listado_usuarios,name='list_users'),
    path('nuevo-user/',nuevo_user,name='new_user'),
    path('editar-user/<id>/', editar_user, name= "edit_user"),
    path('eliminar-user/<id>/',eliminar_user, name = 'eliminar_user'),
    
    ]


