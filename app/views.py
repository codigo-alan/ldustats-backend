from rest_framework import viewsets
from rest_framework.response import Response
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
    """ def get_queryset(self):
        ids = self.request.query_params.get('ids', None)
        if ids != None:
            ids = ids.split(',')
            queryset = File.objects.all().filter(id__in=ids)
            return queryset
        else:
            return File.objects.all() """

class SessionView(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    queryset = Session.objects.all()

class SessionByPlayerView(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    
    def get_queryset(self):
        idParam = self.kwargs['id']
        queryset = Session.objects.all().filter(idPlayer= idParam).order_by('distance')
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
        #TODO works properly, but shows an error.
        ids = self.request.query_params.get('ids').split(',')
        #ids = [ int(x) for x in ids.split(',') ] #converts each id in the list, to an int
        queryset = File.objects.all().filter(id__in=ids)
        return queryset
