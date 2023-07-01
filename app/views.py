from rest_framework import viewsets
from rest_framework.response import Response
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

class SessionByPlayerView(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    
    def get_queryset(self):
        idParam = self.kwargs['id']
        queryset = Session.objects.all().filter(idPlayer= idParam)
        return queryset