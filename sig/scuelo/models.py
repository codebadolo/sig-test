from urllib import request
from django.db import models
from django.contrib import messages

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
    date_enquete = models.DateTimeField(blank=True)  # is  added right after
    condition_eleve = models.CharField(
        max_length=4,
        choices=CONDITION_ELEVE
    )
    sex = models.CharField(max_length=1, choices=SEX)
    date_naissance = models.DateField()
    cs_py = models.CharField(max_length=6, choices=CS_PY)
    hand = models.CharField(max_length=2, choices=HAND  , default="")
    annee_inscr = models.CharField(max_length=4)  # the inscrption year
    parent = models.CharField(max_length=34, null=False)
    tel_parent = models.CharField(max_length=24, null=False)
    type_ecole = models.CharField(max_length=14, choices=TYPE_ECOLE)
    nom_classe = models.CharField(max_length=4, choices=NOM_CLASSE)
    note_eleve = models.CharField(max_length=240, blank=True ,default='')
    
    
    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
    @property
    def an_insc(self):
        return self.annee_inscr.year
    
    '''
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        messages.success(request, f'vous avez enregister l\'eleve {self.nom} {self.prenom} de la classe  de  {self.nom_classe}') 
    '''
    def get_queryset(self, request):
        # Group students by nom_classe
        queryset = Eleve.objects.all().prefetch_related('nom_classe')  # Prefetch for efficiency
        grouped_queryset = {}
        for eleve in queryset:
            classe = eleve.nom_classe.pk  # Get the primary key of nom_classe
            if classe not in grouped_queryset:
                grouped_queryset[classe] = []
            grouped_queryset[classe].append(eleve)
        return grouped_queryset
    
    
    class Meta:
        verbose_name = 'Eleve'
        # order_by = 'nom_classe'
        
        verbose_name_plural = 'Eleves'



class Paiement(models.Model):
    causal = models.CharField(max_length=34, choices=CAUSUAL)

    montant = models.PositiveBigIntegerField()
    date_paiement = models.DateTimeField()
    note_paiement = models.CharField(max_length=200, blank=True)
    eleve_payment = models.ForeignKey(Eleve, on_delete=models.CASCADE,  default=1 )
    
    
    
    class Meta:
        verbose_name = 'Paiement'
        #order_by = 'nom_classe'
        
        verbose_name_plural = 'Paiements'


       
    def __str__(self):
        return f"{self.causal} {self.montant}"
     