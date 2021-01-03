from rest_framework import viewsets

from .serializers import LanguageSerializer
from .models import Language

class LanguageViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
