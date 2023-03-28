from django.db import models
from django.db.models import CharField
from django.db.models import ImageField
from django.db.models import URLField

class Post(models.Model):
    
    title=CharField