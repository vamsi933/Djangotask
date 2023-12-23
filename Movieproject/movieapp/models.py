from django.db import models

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    budget = models.IntegerField()
    heroname = models.CharField(max_length=100)
    no_of_hits= models.IntegerField()