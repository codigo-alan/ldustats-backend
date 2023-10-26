from rest_framework import serializers
from .models import Player, File, Session
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        #Extra data to the response
        data['username'] = self.user.get_username()
        data['isStaff'] = self.user.is_staff
        data['isSuperuser'] = self.user.is_superuser
        return data
    

class PlayerSerializer(serializers.ModelSerializer):
    #sessions = serializers.PrimaryKeyRelatedField(many=True, queryset=Session.objects.all())
    class Meta:
        model = Player # model to serialize
        fields = '__all__' # fields of model to serialize, all in this case
        #fields = ('id', 'name', 'sessions') # fields of model to serialize, id and name in this case

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
    #playerId = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all())
    class Meta:
        model = Session
        fields = '__all__'
        #fields = ('id', 'name', 'playerId') # fields of model to serialize, id and name in this case


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True)
    password = serializers.CharField(
        min_length=8)
    
    """ def validate_password(self, value):
        return make_password(value) """

    class Meta:
        model = get_user_model() #get user model obtains the model default of User from Django
        #fields = ('username', 'password')
        fields = '__all__'