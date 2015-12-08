from django.db import models

from operatori.models import Operatore
from ordini.models import Ordine

# Create your models here.

class Impianto(models.Model):
    codice = models.CharField(max_length=10, unique=True)
    descrizione = models.CharField(max_length=20)

    def __str__(self):
        return self.codice + ": " + self.descrizione

    class Meta:
        ordering = ["codice"]
        verbose_name = "impianto"
        verbose_name_plural = "impianti"

class Pannello(models.Model):
    codice = models.CharField(max_length=10, unique=True)
    acceso = models.BooleanField(default=False)
    allarme = models.BooleanField(default=False)
    impianto = models.OneToOneField(Impianto)
    operatore = models.ForeignKey(Operatore, null=True, blank=True)
    ordine = models.ForeignKey(Ordine, null=True, blank=True)
    ip = models.GenericIPAddressField(default='0.0.0.1')

    def __str__(self):
        return self.codice + ": " + self.ip

    class Meta:
        verbose_name = "pannello"
        verbose_name_plural = "pannelli"
