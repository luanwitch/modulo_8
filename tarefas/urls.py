from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('exercicio-post/', views.exercicio_post_view, name='exercicio_post'),
]