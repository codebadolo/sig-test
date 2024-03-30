from rest_framework import viewsets, generics
from .models import Eleve , Classe 
from .serializers import EleveSerializer , ClasseSerializer

from rest_framework import generics
from .models import Classe, Eleve, Paiement
from .serializers import ClasseSerializer, EleveSerializer, PaiementSerializer

class ClasseListView(generics.ListAPIView):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer

class EleveListView(generics.ListAPIView):
    serializer_class = EleveSerializer

    def get_queryset(self):
        class_id = self.kwargs['class_id']
        return Eleve.objects.filter(classe_id=class_id)

class EleveDetailView(generics.RetrieveAPIView):
    queryset = Eleve.objects.all()
    serializer_class = EleveSerializer

class PaiementCreateView(generics.CreateAPIView):
    serializer_class = PaiementSerializer
