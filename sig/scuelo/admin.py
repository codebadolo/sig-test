from django.contrib import admin
from .models import Paiement, Eleve
from django.contrib import admin

class  PaimentInline(admin.TabularInline):
    model = Paiement
    '''raw_id_fields = ['causal', 'montant',
                    'date_paiement',
                    'note_paiement']
    '''

class SicAdminArea(admin.AdminSite):
    site_header = 'SICS NASSARA'
    site_title = 'SICS NASSARA'
    index_title = 'SICS NASSARA'


sics_site = SicAdminArea(name='SICS NASSARA')


class EleveAdmin(admin.ModelAdmin):
    fieldsets = (
        ('INFORMATIONS DE  BASE', {
            'fields': ('nom', 'prenom', 'sex',
                       'date_naissance'
            ),
        }
         ),
        ('INFORMATION   CLASSE', {
            'fields': ('type_ecole', 'nom_classe'
                       ,'annee_inscr'),
        }
         ),
        ('INFORMATION SOCIALE', {
            'fields': ('condition_eleve', 'cs_py' ,'hand'
                       ,'date_enquete'),
        }
         ),
        ('INFORMATION PARENT', {
            'fields': ('parent', 'tel_parent',
                       ),
        }
         )
    )
    
    inlines =[PaimentInline ,]
    
    
    list_display = [
        'nom', 'prenom', 'condition_eleve',
        'sex','type_ecole', 'nom_classe'
    ]
    
    #list_select_related =
    search_fields = ['nom', 'prenom']
    list_filter = ['nom_classe']
    ordering= ["nom_classe"]
    #list_select_related = ['paiment_set']
    #list_select_related = ['paiement_set']
    # Add 'nom_classe' to filter by class
    
    def __str__( self ):
        return self.name 
   

class PaiementAdmin(admin.ModelAdmin):
    
    list_display = [
        'causal', 'montant',
        'date_paiement','note_paiement'
    ]
    #filter_horizontal = True
    
    
    list_select_related= ["eleve_payment"]
    #inlines = [ EleveInline ,]
    
    def get_list_display(self, request):
        # Add 'section' to list_display
        return super().get_list_display(request) + ['section']
    
    def section(self, obj):
        # Custom method to display the class section
        return obj.nom_classe
    
    section.admin_order_field = 'nom_classe'  # Enable sorting by section
    
    def get_list_display_links(self, request, list_display):
        # Disable editing links for 'section' column
        return ['nom']


sics_site.register(Paiement)
#sics_site.register(Paiement, PaiementAdmin)


sics_site.register(Eleve, EleveAdmin)
#admin.site.register(Eleve, EleveAdmin)
#admin.site.site_header = 'SICS NASSARA'
#admin.site.site_title = 'SICS NASSARA'
#admin.site.index_title = 'SICS NASSARA'


#admin.site. = 'Admin Customization'
