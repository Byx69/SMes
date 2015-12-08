from django.db import models

from impianti.models import Impianto
from ordini.models import Ordine

# Create your models here.

class Scheda(models.Model):
    impianto = models.ForeignKey(Impianto)
    ordine = models.ForeignKey(Ordine)
    priorita = models.PositiveIntegerField(default=1)
    data_inizio = models.DateTimeField(null=True, blank=True)
    data_fine = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.impianto.codice + " / " + self.ordine.numero + " : " + str(self.priorita)

    class Meta:
        verbose_name = "scheda"
        verbose_name_plural = "schede"
