from django.db import models

# Create your models here.

TIPO =(
    ('O', 'Operaio'),
    ('A', 'Attrezzista'),
    ('Q', 'Controllo qualità'),
    )
    

class Operatore(models.Model):
    nome = models.CharField(max_length=20, unique=True)
    tessera = models.CharField(max_length=10, default='1234567890') # Tessera identificazione
    tipo = models.CharField(max_length=1, choices=TIPO, default='O')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome"]
        verbose_name = "operatore"
        verbose_name_plural = "operatori"
