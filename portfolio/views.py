from django.shortcuts import render
from .models import Project

def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html')
    return render(request, 'portfolio/index.html', {'projects': projects})

