from django.db import models


# Create your models here.
# Creation du models de participant

class User(models.Model):
    nom = models.CharField(max_length=128)
    prénom = models.CharField(max_length=128)
    numéro = models.IntegerField()
    adresse_email = models.CharField(max_length=250)