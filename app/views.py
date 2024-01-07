from rest_framework import viewsets
from .serializer import TeamSerializer, PlayerSerializer, SessionSerializer, FileSerializer, CustomObtainPairSerializer, UserSerializer
from .models import Team, Player, Session, File
import logging
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView
from django.db import models

logger = logging.getLogger(__name__)

class TeamView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TeamSerializer
    queryset = Team.objects.all().order_by('id')

class PlayerView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PlayerSerializer
    queryset = Player.objects.all().order_by('name')

    """ def get_queryset(self):
        #print(self.action)
        #teamParam = self.request.query_params.get('teamParam') 
        queryset = Player.objects.all().order_by('name')
        return queryset """
   
    def retrieve(self, request, pk=None):
        try:
            instance = Player.objects.get(pk=pk)
            serializer = self.serializer_class(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Player.DoesNotExist:
            return Response({'detail': 'Player not found.'}, status=status.HTTP_404_NOT_FOUND)
        
    def destroy(self, request, pk=None):
        try:
            instance = Player.objects.get(pk=pk)
            instance.delete()
            return Response({'detail': 'Player deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Player.DoesNotExist:
            return Response({'detail': 'Player not found.'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            #request.data["team"] = request.data["team"].lower() # convert to lower the team
            instance = Player.objects.get(pk=pk)
            serializer = self.serializer_class(instance, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Player.DoesNotExist:
            return Response({'detail': 'Player not found.'}, status=status.HTTP_404_NOT_FOUND)

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

class UserView(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            createdUser = serializer.create()
            return Response({"message": "Usuario registrado exitosamente", "user": createdUser}, status=status.HTTP_201_CREATED)
        return Response({"message": "Todos los campos son obligatorios", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

    """ def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            usernameValidated = serializer.validated_data['username']
            passwordValidated = serializer.validated_data['password']
            User.objects.create_user(username=usernameValidated, password=passwordValidated)
            return Response({"mensaje": "Usuario registrado exitosamente"}, status=status.HTTP_201_CREATED)
        return Response({"mensaje": "Todos los campos son obligatorios", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
 """

    """ def create(self):
        # obtain the data from the request
        username = self.request.query_params.get('username', None)
        password = self.request.query_params.get('password', None)
        
        # Validate data

        if not username or not password:
            return Response({"mensaje": "Todos los campos son obligatorios"}, status=status.HTTP_400_BAD_REQUEST)

        # Create new user in db
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return Response({"mensaje": "Usuario registrado exitosamente"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({"mensaje": "Error al registrar el usuario"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) """

class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = CustomObtainPairSerializer

class HistoricalInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        refParam = self.request.query_params.get('refParam', None)
        
        if refParam is not None:
            try:
                sessionsFiltered = Session.objects.filter(idPlayer=refParam)

                maxSpeedPlayer = round(sessionsFiltered.aggregate(max_vel=models.Max('maxSpeed'))['max_vel'], 2)

                maxDistancePlayer = round(sessionsFiltered.aggregate(max_dis=models.Max('totalDistance'))['max_dis'], 2)

                maxSprintsPlayer = sessionsFiltered.aggregate(max_sprints=models.Max('spints'))['max_sprints']

                maxSprintsDistancePlayer = round(sessionsFiltered.aggregate(max_sprints_distance=models.Max('sprintDistance'))['max_sprints_distance'], 2)

                maxAcc = sessionsFiltered.aggregate(max_acc=models.Max('accelerations'))['max_acc']

                maxDec = sessionsFiltered.aggregate(max_dec=models.Max('decelerations'))['max_dec']

            except:
                return Response({"message": f"Player without sessions"}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(
                {"maxSpeed": f"{maxSpeedPlayer} km/h", 
                 "totalDistance": f"{maxDistancePlayer} m", 
                 "sprints": f"{maxSprintsPlayer}", 
                 "sprintsDistance": f"{maxSprintsDistancePlayer} m",
                 "maxAcc": f"{maxAcc}",
                 "maxDec": f"{maxDec}"}, status=status.HTTP_200_OK)
            
        else: return Response({"message": f"GET request SIN parámetro {refParam}"}, status=status.HTTP_400_BAD_REQUEST)
