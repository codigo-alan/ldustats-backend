from rest_framework import viewsets
from .serializer import PlayerSerializer, SessionSerializer, FileSerializer
from .models import Player, Session, File
import logging

logger = logging.getLogger(__name__)

# Create your views here.
class PlayerView(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

class FileView(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()


class SessionByPlayerView(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    
    def get_queryset(self):
        idParam = self.kwargs['id']
        queryset = Session.objects.all().filter(idPlayer= idParam).order_by('date')
        return queryset
    
class SessionByFileView(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    
    def get_queryset(self):
        idParam = self.kwargs['id']
        queryset = Session.objects.all().filter(idFile= idParam)
        return queryset
    
class FilesByIdsView(viewsets.ModelViewSet):
    serializer_class = FileSerializer

    def get_queryset(self):

        ids = self.request.query_params.get('ids')

        if (ids != ''):
            #ids = [ int(x) for x in ids.split(',') ] #converts each id in the list, to an int
            ids = ids.split(',')
        else:
            ids = []

        queryset = File.objects.filter(id__in=ids)
        
        return queryset

    
class SessionView(viewsets.ModelViewSet):
    serializer_class = SessionSerializer

    def get_queryset(self):
        idPlayerParam = self.request.query_params.get('idplayer', None)
        idFileParam = self.request.query_params.get('idfile', None)
        if idPlayerParam != None and idFileParam != None:
            queryset = Session.objects.filter(idPlayer= idPlayerParam, idFile= idFileParam)
            return queryset
        elif idPlayerParam == None and idFileParam != None:
            return Session.objects.filter(idFile= idFileParam)
        elif idPlayerParam != None and idFileParam == None:
            return Session.objects.filter(idPlayer= idPlayerParam)
        else:
            return Session.objects.all()

    
