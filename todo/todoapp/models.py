from django.db import models

# Create your models here.

class Todo(models.Model):
    Titles = models.CharField(max_length=25)
    Description = models.CharField(max_length=100)
