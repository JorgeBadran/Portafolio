from django.shortcuts import render
from .models import Project

def home(resquest):
    projects = Project.objects.all()
    return render(resquest,'home.html', {'projects': projects})#ignore
