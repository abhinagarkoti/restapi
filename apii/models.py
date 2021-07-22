from django.db import models

# Create your models here.

from django.db import models
from django.db.models.fields import CharField


class Snippet(models.Model):
    name= models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    idd=models.CharField(max_length=100)
    
    class meta:
        ordering=('id')
