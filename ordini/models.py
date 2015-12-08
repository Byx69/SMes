from django.db import models

from lavorazioni.models import Lavorazione

# Create your models here.

class Ordine(models.Model):
        numero = models.CharField(max_length=10, unique=True)
        data = models.DateField()
        termine = models.DateField()
        lavorazione = models.ForeignKey(Lavorazione)
        quantita = models.DecimalField(max_digits=9, decimal_places=2, default=1)
        quantita_ok = models.DecimalField(max_digits=9, decimal_places=2, default=0)
        quantita_ko = models.DecimalField(max_digits=9, decimal_places=2, default=0)
        data_apertura = models.DateField(null=True, blank=True)
        data_chiusura = models.DateField(null=True, blank=True)
        
        def __str__(self):
                return self.numero + " del " + self.data.strftime("%y/%m/%d")

        class Meta:
                ordering = ["numero"]
                verbose_name = "ordine"
                verbose_name_plural = "ordini"
