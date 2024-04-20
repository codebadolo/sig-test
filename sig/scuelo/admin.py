from django.contrib import admin
from  .models import Paiement , Eleve
from django.contrib import admin

class SicAdminArea(admin.AdminSite):
    site_header = 'SICS NASSARA'
    site_title = 'SICS NASSARA'
    index_title = 'SICS NASSARA'

sics_site = SicAdminArea(name='SICS NASSARA')
sics_site.register(Paiement)

class EleveAdmin(admin.ModelAdmin):
    list_display = [
        'nom', 'prenom', 'condition_eleve',
        'sex','type_ecole', 'nom_classe'
    ] # 
    search_fields = ['nom', 'prenom']
    list_filter = ['nom_classe']
    list_select_related = ['paiement_set']
    # Add 'nom_classe' to filter by class

sics_site.register(Eleve , EleveAdmin)
#admin.site.register(Eleve, EleveAdmin)
#admin.site.site_header = 'SICS NASSARA'
#admin.site.site_title = 'SICS NASSARA'
#admin.site.index_title = 'SICS NASSARA'


#admin.site. = 'Admin Customization'