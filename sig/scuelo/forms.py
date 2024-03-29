from .models  import Eleve  , Paiement ,  Classe
from django  import  forms

class EleveForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = [
            'nom', 'prenom', 'condition_eleve',
            'sex', 'date_naissance', 'cs_py', 'hand', 
            'parent', 'tel_parent'
                  
        ]
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'condition_eleve': 'Condition de l\'élève',
            'sex': 'Sexe',
            'date_naissance': 'Date de naissance',
            'cs_py': 'CS/PY',
            'hand': 'Handicap',
            'parent': 'Nom du parent',
            'tel_parent': 'Téléphone du parent',
        }
        placeholders = {
            'nom': 'Entrez votre nom',
            'prenom': 'Entrez votre prénom',
            'cs_py': 'CS ou PY',
            'parent': 'Nom du parent',
            'tel_parent': 'Téléphone du parent',
        }
        #