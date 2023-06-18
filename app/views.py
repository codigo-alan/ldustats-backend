from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
import csv
from .serializer import PlayerSerializer
from .models import Player

# Create your views here.
class PlayerView(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

@api_view(['POST'])
def upload_csv(request):
    file = request.FILES['file']

    # Decodifica el archivo CSV
    decoded_data = file.read().decode('utf-8')

    # Procesa los datos del CSV
    csv_data = csv.reader(decoded_data.splitlines())
    data_list = list(csv_data)

    # Realiza las operaciones necesarias con los datos
    print(data_list)

    return Response({'message': 'Archivo CSV recibido y decodificado correctamente.'})