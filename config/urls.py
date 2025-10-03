from turtle import home
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tarefas.urls")), 
    path("", home, name="home"),
]
