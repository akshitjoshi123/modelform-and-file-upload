from django.db import models
from django.db.models.aggregates import Max
from django.forms import ModelForm
from django.db.models import fields

# Create your models here.

class feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()  
    desc = models.TextField(max_length=500)

    def __str__(self):
        return self.name
