from rest_framework import viewsets, generics
from .models import Eleve , Classe 
from .serializers import EleveSerializer , ClasseSerializer

class EleveViewSet(viewsets.ModelViewSet):
    queryset = Eleve.objects.all()
    serializer_class = EleveSerializer

class EleveDetailView(generics.RetrieveAPIView):
    queryset = Eleve.objects.all()
    serializer_class = EleveSerializer

class ClasseViewSet(viewsets.ModelViewSet):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer