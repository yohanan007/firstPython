from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Prospet(models.Model):
    nom = models.CharField(max_length = 200)
    prenom = models.CharField(max_length = 200)
    date_de_naissance = models.DateTimeField(default=timezone.now, verbose_name="date de naissance")
    date_de_creation =  models.DateField(auto_now = True)
    date_de_maj = models.DateField(auto_now_add = True)
