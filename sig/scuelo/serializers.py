
from rest_framework import serializers
from .models import Eleve ,  Classe

class EleveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eleve
        fields = '__all__'
        
class ClasseSerializer(serializers.ModelSerializer):
    eleve_set = EleveSerializer(many=True, read_only=True)
    class Meta:
        model = Classe
        fields = [
            'id', 'type_ecole' , 'nom_classe', 
            'ordre_classe','eleve_set'
        ]
        
        
    
