from django.db import models

class Remedio(models.Model):
    nome = models.CharField(max_length=255)
