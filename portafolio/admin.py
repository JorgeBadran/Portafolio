from django.contrib import admin
from .models import Project

#Importamop el modelo project a el panel de administrador(django_porfolio)
admin.site.register(Project)
