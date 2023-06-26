from rest_framework import serializers
from .models import Player, File, Session

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player # model to serialize
        fields = '__all__' # fields of model to serialize, all in this case
        # fields = ('id', 'name') # fields of model to serialize, id and name in this case

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'