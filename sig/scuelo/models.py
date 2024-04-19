from django.db import models

TYPE_ECOLE = (

    ("MATERNELLE", "MATERNELLE"),
    ("PRIMAIRE", "PRIMAIRE"),

)

CONDITION_ELEVE = (
    ("CONF", "CONF"),
    ("ABAN", "ABAN"),
    ("PROP", "PROP"),
)
# DA  ==   DEFFISCIENCE AUDITIVE
# DM ==  DEF MOTRICE
# DL ==   TROUBLE DU LANGUAGE
# DV ==  VISUELLE
# DI == INTELLECTUELLE

HAND = (
    ("DA", "OUI"),
    ("DM", "NON"),
    ("DM", "NON"),
    ("DM", "NON"),

)
CS_PY = (
    ("CS", "CS"),
    ("Extra", "EXTRA"),
    ("PY", "PY"),
)
SEX = (
    ("F", "F"),
    ("M", "M"),
)

CAUSUAL = (
    ("insc", "inscription"),
    ("sco", "scolarite"),
    ("ten", "tenue"),
    ("can", "cantine"),

)

NOM_CLASSE = (
    ("PS", "PS"),
    ("MS", "MS"),
    ("GS", "GS"),
    ("CP1", "CP1"),
    ("CP2", "CP2"),
    ("CE1", "CE1"),
    ("CE2", "CE2"),
    ("CM1", "CM1"),
    ("CM2", "CM2"),

)


class Eleve(models.Model):
    nom = models.CharField(max_length=34, null=False)
    prenom = models.CharField(max_length=34, null=False)
    # etat =  models.CharField(max_length  =  10  , choice = )
    date_enquete = models.DateTimeField(auto_now_add=True)  # is  added right after
    condition_eleve = models.CharField(
        max_length=34,
        choices=CONDITION_ELEVE
    )
    sex = models.CharField(max_length=10, choices=SEX)
    date_naissance = models.DateField()
    cs_py = models.CharField(max_length=34, choices=CS_PY)
    hand = models.CharField(max_length=34, choices=HAND)
    annee_inscr = models.DateField() # the inscrption year
    parent = models.CharField(max_length=34, null=False)
    #nro_tenu = models.CharField()
    tel_parent = models.CharField(max_length=12, null=False)

    type_ecole = models.CharField(max_length=14, choices=TYPE_ECOLE)
    nom_classe = models.CharField(max_length=34, choices=NOM_CLASSE)
    # ordre_classe = models.CharField(max_length=4)
    #eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)



'''
class Classe(models.Model):
    # id= models.CharField(max_length =  34 , primary_key  =  True)
    type_ecole = models.CharField(max_length=14, choices=TYPE_ECOLE)
    nom_classe = models.CharField(max_length=34, choices=NOM_CLASSE)
    ordre_classe = models.CharField(max_length=4)
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)

    class Meta:
        pass
'''

# department=models.ForeignKey(Department, on_delete=models.CASCADE)

class Paiement(models.Model):
    #eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    causal = models.CharField(max_length=34, choices=CAUSUAL)
    montant = models.PositiveBigIntegerField(max_length=34)
    date_paiement = models.DateTimeField(auto_now_add=True)
    note_Paiement = models.CharField(max_length=200, blank=True)
