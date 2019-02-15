from django.db import models

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=100)
    genus = models.CharField(max_length=100)
    is_domesticated = models.BooleanField(default=True)
    objects = models.Manager()
    def __str__(self):
        return self.name
