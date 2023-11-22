from rest_framework import viewsets
from .serializer import PlayerSerializer, SessionSerializer, FileSerializer, CustomObtainPairSerializer
from .models import Player, Session, File
import logging
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView


logger = logging.getLogger(__name__)

# Create your views here.
class PlayerView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

class FileView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FileSerializer
    queryset = File.objects.all().order_by('-date')

class SessionByPlayerView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SessionSerializer
    
    def get_queryset(self):
        idParam = self.kwargs['id']
        queryset = Session.objects.filter(idPlayer= idParam).order_by('date')
        return queryset
    
class FilesByIdsView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FileSerializer

    def get_queryset(self):

        ids = self.request.query_params.get('ids')

        if (ids != ''):
            #ids = [ int(x) for x in ids.split(',') ] #converts each id in the list, to an int
            ids = ids.split(',')
        else:
            ids = []

        queryset = File.objects.filter(id__in=ids).order_by('-date')
        
        return queryset
  
class SessionView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
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
        
class SessionIntervalsView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SessionSerializer

    def get_queryset(self):
        nameParam = self.request.query_params.get('playerName')
        initDateParam = self.request.query_params.get('initDate')
        endDateParam = self.request.query_params.get('endDate')
        return Session.objects.filter(name__iexact=nameParam, date__gte= initDateParam, date__lte= endDateParam).order_by('date')

class RegisterUserView(viewsets.ViewSet):
    permission_classes = [IsAdminUser]  # Allow access without authentication

    def post(self):
        # obtain the data from the request
        username = self.request.query_params.get('username', None)
        email = self.request.query_params.get('email', None)
        password = self.request.query_params.get('password', None)
        

        # Validate data

        if not username or not email or not password:
            return Response({"mensaje": "Todos los campos son obligatorios"}, status=status.HTTP_400_BAD_REQUEST)

        # Create new user in db
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            #TODO here is neccessary make a LOGIN of the recently added User
            return Response({"mensaje": "Usuario registrado exitosamente"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"mensaje": "Error al registrar el usuario"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = CustomObtainPairSerializer