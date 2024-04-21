from django.db import models

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
    ("DA", "DA"),
    ("DM", "DM"),
    ("DL", "DL"),
    ("DV", "DV"),

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

TYPE_ECOLE = (
    ("MATERNELLE", "MATERNELLE"),
    ("PRIMAIRE", "PRIMAIRE"),

)



class Eleve(models.Model):
    nom = models.CharField(max_length=34, null=False)
    prenom = models.CharField(max_length=34, null=False)
    date_enquete = models.DateTimeField()  # is  added right after
    condition_eleve = models.CharField(
        max_length=34,
        choices=CONDITION_ELEVE
    )
    sex = models.CharField(max_length=10, choices=SEX)
    date_naissance = models.DateField()
    cs_py = models.CharField(max_length=34, choices=CS_PY)
    hand = models.CharField(max_length=34, choices=HAND)
    annee_inscr = models.DateField()  # the inscrption year
    parent = models.CharField(max_length=34, null=False)
    tel_parent = models.CharField(max_length=12, null=False)
    type_ecole = models.CharField(max_length=20, choices=TYPE_ECOLE)
    nom_classe = models.CharField(max_length=34, choices=NOM_CLASSE)
    note_eleve = models.CharField(max_length=240, null=True)
    
    def __str__(self):
        return self.nom

    #@prope rty
    #def effectif(self):
    #pass
    class Meta:
        verbose_name = 'Eleve'
        #order_by = 'nom_classe'
        
        verbose_name_plural = 'Eleves'
        


class Paiement(models.Model):
    causal = models.CharField(max_length=34, choices=CAUSUAL)
    montant = models.PositiveBigIntegerField()
    date_paiement = models.DateTimeField(auto_now_add=True)
    note_paiement = models.CharField(max_length=200, blank=True)
    eleve_payment = models.ForeignKey(Eleve, on_delete=models.CASCADE,  default=1 )
    
    
    def __str__(self) -> str:
        return  self.causal 
    
     