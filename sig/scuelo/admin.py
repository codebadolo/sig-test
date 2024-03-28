from django.contrib import admin
from  .models import Paiement , Eleve , Classe
# Register your models here.
admin.site.register(Paiement)
admin.site.register(Eleve)
admin.site.register(Classe)