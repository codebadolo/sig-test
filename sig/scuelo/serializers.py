
from rest_framework import serializers
from .models import Eleve

class EleveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eleve
        fields = '__all__'
        
        
        #fields = ['id', 'nom', 'prenom','date_enquete', 'condition_eleve', 'sex', 'date_naissance', 'cs_py', 
        #          'hand', 'annee_inscr', 'parent', 
        #          'tel_parent']
