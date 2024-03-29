from rest_framework import viewsets, generics
from .models import Eleve
from .serializers import EleveSerializer

class EleveViewSet(viewsets.ModelViewSet):
    queryset = Eleve.objects.all()
    serializer_class = EleveSerializer

class EleveDetailView(generics.RetrieveAPIView):
    queryset = Eleve.objects.all()
    serializer_class = EleveSerializer
