from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Game, UserGame, Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']




class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'



class UserGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGame
        fields = '__all__'




class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

