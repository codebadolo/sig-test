from rest_framework import serializers
from .models import Classe, Eleve, Paiement


class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields = '__all__'


class EleveSerializer(serializers.ModelSerializer):
    paiement = PaiementSerializer(many=True, read_only=True)

    class Meta:
        model = Eleve
        fields = ['id', 'nom', 'prenom', 'date_enquete', 'condition_eleve',
                  'sex', 'date_naissance', 'cs_py', 'hand',
                  'annee_inscr', 'parent', 'tel_parent', 'paiements'
        ]


class ClasseSerializer(serializers.ModelSerializer):
    eleves = EleveSerializer(many=True, read_only=True)

    class Meta:
        model = Classe
        fields = ['id', 'nom_classe', 'ordre_classe', 'type_ecole', 'eleves']


class ClassCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = ['id', 'nom_classe', 'ordre_classe', 'type_ecole']
