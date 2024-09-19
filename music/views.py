from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import Music
from .serializers import MusicSerializer
from django_filters.rest_framework import DjangoFilterBackend


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_filds = ['titulo']
    search_fields =['titulo', 'album']


