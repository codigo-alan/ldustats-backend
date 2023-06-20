from rest_framework import viewsets

from rest_framework.response import Response
import csv
from .serializer import PlayerSerializer, SessionSerializer
from .models import Player, Session

# Create your views here.
class PlayerView(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

class SessionView(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    queryset = Session.objects.all()

