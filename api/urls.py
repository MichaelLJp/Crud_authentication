from django.urls import path
from .views import PersonaList, listado_books

urlpatterns = [
  path('/persona/',PersonaList.as_view(), name = 'persona_list'),
]