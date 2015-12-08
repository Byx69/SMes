from django.contrib import admin

# Register your models here.

from impianti.models import Impianto, Pannello

admin.site.register(Impianto)

admin.site.register(Pannello)
