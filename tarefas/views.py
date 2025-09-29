from django.http import HttpResponse

def index(request):
    return HttpResponse("Página inicial de tarefas 🚀")

def post_view(request):
    return HttpResponse("Hello World")