from rest_framework import viewsets, generics
from .models import Eleve, Classe
from .serializers import EleveSerializer, ClasseSerializer

from rest_framework import generics
from .models import Classe, Eleve, Paiement
from .serializers import (

                          ClasseSerializer,
                          EleveSerializer,
                          PaiementSerializer,
                          ClassCreationSerializer
)


# functionalities to be developped
# if we click  on the class  name
# we  have the list of  the students  from  this class
# and  we can the select the needed student and  be able to update
# - in this student informations must be able to    view    older payments and
# - be able to add  others  one for this  student directly  in his   view pages
# under the payments we have the total of all payments linked to that particular student


# in order to record a  student
#  track his   primary information
# be able to  a  school and   a    classe and  link them rationally
# the  classes and  schools  are  list and can be selected
# the class of the student can be  updated   with in the student  update section

#list   of  the classes

#list of student of a class

class ClasseListView(generics.ListAPIView):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer

class ClasseCreateView(generics.CreateAPIView):
    serializer_class = ClassCreationSerializer


class EleveListView(generics.ListAPIView):
    serializer_class = EleveSerializer
    #  be able to   update
    #  view  the payment  of that particular student
    #add a payment   to this student
    #  total of payement
    #changer class

    def get_queryset(self):
        class_id = self.kwargs['class_id']
        return Eleve.objects.filter(classe_id=class_id)


class EleveDetailView(generics.RetrieveAPIView):
    queryset = Eleve.objects.all()
    serializer_class = EleveSerializer
    # be also able to


class PaiementCreateView(generics.CreateAPIView):
    serializer_class = PaiementSerializer
    # payments  are linked to  a particular students
    # payment delai only on  nassara students
    # and a question that i  have to ask is how  it is deal
    # external student  how   their are deal

