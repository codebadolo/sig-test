from django.db import models


TYPE_ECOLE =( 
          
    ("MATERNELLE", "CONF"),
    ("PRIMAIRE", "ABAN"),
    ("PROP", "PROP"),
)

    
CONDITION_ELEVE =(
    ("CONF", "CONF"),
    ("ABAN", "ABAN"),
    ("PROP", "PROP"),
)
HAND =(        
    ("OUI", "OUI"),
    ("NON", "NON"),
)
HAND =(     
    ("CS", "CS"),
    ("Extra", "EXTRA"),
    ("PY", "PY"), 
)
SEX =(      
    ("Fille", "Fille"),
    ("Garcon", "Garcon"),
)

CAUSUAL =(
    ("insc", "inscription"),
    ("sco", "scolarite"),
    ("ten", "tenue"),
    ("can", "cantine"),
    
)

class Eleve(models.Model):
    nom	= models.CharField(max_length =  34 ,   null  = False)
    prenom	 = models.CharField(max_length =  34 ,   null  = False )
    #etat =  models.CharField(max_length  =  10  , choice = )
    date_enquete = models.DateTimeField(auto_now_add =  True)
    condition_eleve	= models.CharField(
        max_length =  34 ,
        choices = CONDITION_ELEVE
    )
    sex= models.CharField(max_length =  10 , choices =  SEX)
    date_naissance	= models.DateField()
    cs_py = models.CharField(max_length =  34)
    hand = models.CharField(max_length =  34  , choices =  HAND )
    annee_inscr = models.DateField( auto_now_add = True)
    parent = models.CharField(max_length =  34 ,   null  = False)
    tel_parent	 = models.CharField(max_length =   12 ,   null  = False)
   
   
    
   
class Classe(models.Model):
    
    #id= models.CharField(max_length =  34 , primary_key  =  True)
    
    nom_classe = models.CharField(max_length =  34)
    ordre_classe =  models.CharField(max_length =  4)
    eleve = models.ForeignKey(Eleve ,on_delete =models.CASCADE )
    type_ecole = models.CharField(max_length =  14 ,  choices  = TYPE_ECOLE  ) 
    
# department=models.ForeignKey(Department, on_delete=models.CASCADE)

class Paiement(models.Model):
    eleve = models.ForeignKey( Eleve  ,  on_delete =  models.CASCADE  )
    causal = models.CharField(max_length =  34 , choices = CAUSUAL)
    montant	 = models.CharField(max_length =  34)
    date_paiement = models.DateTimeField(auto_now_add =  True)
    note_Paiement = models.CharField(max_length =  200  , blank =  True)