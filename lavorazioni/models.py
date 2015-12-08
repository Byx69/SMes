from django.db import models

# Create your models here.

class Lavorazione(models.Model):
    codice = models.CharField(max_length=10, unique=True)
    descrizione = models.CharField(max_length=20)
    tempo = models.DecimalField(max_digits=5, decimal_places=2, default=1) # Tempo di lavorazione in secondi

    def __str__(self):
        return self.codice + ": " + self.descrizione

    def media(self):
        return 3600 / self.tempo # Produzione oraria

    class Meta:
        ordering = ["codice"]
        verbose_name = "lavorazione"
        verbose_name_plural = "lavorazioni"
