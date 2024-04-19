from django.contrib import admin
from  .models import Paiement , Eleve


class EleveAdmin(admin.ModelAdmin):
    list_display = [
        'nom', 'prenom', 'condition_eleve',
        'sex','type_ecole', 'nom_classe'
    ] # 
    search_fields = ['nom', 'prenom']
    list_filter = ['nom_classe']
    list_select_related = ["paiement_set"]
    ordering = ["nom_classe"]
    #readonly_fields = ['paiement_set']  # Display related payments as readonly

    #def paiement_set(self, obj):
        #return obj.paiement_set.all()  # Access related payments using manager
    
    
    # Add 'nom_classe' to filter by class
    def get_group_by(self, request):
        return ['nom_classe']


    # ... other configurations from previous example
admin.site.register(Eleve, EleveAdmin)
admin.site.register(Paiement)

admin.site.site_header = 'SICS NASSARA'
#admin.site. = 'Admin Customization'