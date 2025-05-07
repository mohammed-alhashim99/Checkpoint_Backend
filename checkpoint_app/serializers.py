from rest_framework import serializers
from .models import Game, UserGame, Review
from django.contrib.auth.models import User


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class UserGameCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGame
        fields = '__all__'
        read_only_fields = ['user']

    def validate(self, data):
        user = self.context['request'].user
        game = data.get('game')
        if UserGame.objects.filter(user=user, game=game).exists():
            raise serializers.ValidationError("You already added this game.")
        return data

class UserGameDetailSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)

    class Meta:
        model = UserGame
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    game = GameSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['user']


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['game']
