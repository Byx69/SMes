from django.db import models

# Create your models here.

class Operatore(models.Model):
    nome = models.CharField(max_length=20, unique=True)
    tessera = models.CharField(max_length=10, default='1234567890') # Tessera identificazione

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome"]
        verbose_name = "operatore"
        verbose_name_plural = "operatori"
