from django.http import HttpResponse

def hello_world_view(request):
    return HttpResponse("Hello World!")

def home(request):  
    return HttpResponse("Página inicial funcionando!")