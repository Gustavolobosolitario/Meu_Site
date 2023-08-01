from django.shortcuts import render

def index(request):
    # Lógica da visualização aqui
    return render(request, 'index.html')

# Create your views here.
