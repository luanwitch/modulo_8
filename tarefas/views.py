from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tarefa

def lista_tarefas(request):
    if request.method == 'POST':
        novo_titulo = request.POST.get('titulo')
        Tarefa.objects.create(titulo=novo_titulo)
        return redirect('lista_tarefas')

    tarefas = Tarefa.objects.all().order_by('concluida')
    contexto = {'tarefas': tarefas}
    return render(request, 'tarefas/lista.html', contexto)

def exercicio_post_view(request):
    if request.method == 'POST':
        return HttpResponse("Hello world")

    return render(request, 'tarefas/exercicio_post.html')