from rest_framework import serializers
from .models import Player, File, Session, Team
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
    
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

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
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, required=True)
    isStaff = serializers.BooleanField(default=False)

    def validate_username(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError('El nombre no debe contener números')
        return value
    
    def validate_password(self, value):
        if not any(char.isdigit() for char in value) or not any(char.isalpha() for char in value):
            raise serializers.ValidationError('La contraseña debe contaner letras y números')
        
        if not any(char.isupper() for char in value) or not any(char.islower() for char in value):
            raise serializers.ValidationError('La contraseña debe contener mayúsculas y minúsculas')
        
        if all(char.isalnum() for char in value):
            raise serializers.ValidationError('La contraseña debe contener algún caracter especial')
        return value

    class Meta:
        model = get_user_model() #get user model obtains the model default of User from Django
        #fields = ('username', 'password')
        fields = '__all__'