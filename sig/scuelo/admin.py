from django.contrib import admin
from  .models import Paiement , Eleve
from django.contrib import admin

class EleveAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'condition_eleve', 'sex', 'nom_classe'] # 'type_ecole',
    search_fields = ['nom', 'prenom']
    list_filter = ['nom_classe']  # Add 'nom_classe' to filter by class

admin.site.register(Eleve, EleveAdmin)
