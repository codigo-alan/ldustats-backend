from rest_framework import viewsets
from .serializer import PlayerSerializer
from .models import Player

# Create your views here.
class PlayerView(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()