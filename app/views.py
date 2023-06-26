from rest_framework import viewsets
from .serializer import PlayerSerializer, SessionSerializer, FileSerializer
from .models import Player, Session, File

# Create your views here.
class PlayerView(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

class FileView(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()

class SessionView(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    queryset = Session.objects.all()

