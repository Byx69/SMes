from impianti.models import Impianto
from operatori.models import Operatore
from ordini.models import Ordine

from django.db import models

# Create your models here.

EVENTI = (
    ('ON', 'Impianto spento'),
    ('OFF', 'Impianto acceso'),
    ('ALS', 'Allarme scattato'),
    ('ALR', 'Allarme rientrato'),
    ('OP+', 'Operatore inserito'),
    ('OP-', 'Operatore disinserito'),
    ('ORA', 'Ordine aperto'),
    ('ORO', 'Ordine chiuso'),
    )

class Registrazione(models.Model):
    istante = models.DateTimeField(auto_now_add=True)
    evento = models.CharField(max_length=3, choices=EVENTI)
    impianto = models.ForeignKey(Impianto)
    operatore = models.ForeignKey(Operatore, null=True, blank=True)
    ordine = models.ForeignKey(Ordine, null=True, blank=True)
    quantita_ok = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    quantita_ko = models.DecimalField(max_digits=9, decimal_places=2, default=0)

    def __str__(self):
        return self.istante.strftime("%y/%m/%d-%H:%M") + " > " + self.evento + " x " + self.impianto.codice

    class Meta:
        ordering = ["-istante"]
        verbose_name = "registrazione"
        verbose_name_plural = "registrazioni"
    
