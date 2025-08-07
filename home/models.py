from django.db import models

# Create your models here.

class Rang(models.Model):
    name = (models.CharField(max_length=50))

class Sumka(models.Model):
    name = models.CharField(max_length=110)
    modele = models.TextField()
    rangi = models.ForeignKey(Rang, on_delete=models.PROTECT, related_name='rang')
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
