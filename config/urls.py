# config/urls.py
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from tarefas.views import hello_world_view

def home(request):
    return HttpResponse("Página inicial funcionando!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world_view, name='hello_world'), 
    path('', home, name='home'),  # rota raiz
]
