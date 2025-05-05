from django.forms import ValidationError
from rest_framework import serializers
from .models import Game, UserGame, Review
from django.contrib.auth.models import User
from rest_framework import serializers

# 🎮 Game Serializer
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

# 👤 UserGame Serializer
class UserGameCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGame
        fields = '__all__'
        read_only_fields = ['user']

class UserGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGame
        fields = '__all__'
        def validate(self, data):
            user = data.get('user')
            game = data.get('game')
            if UserGame.objects.filter(user=user, game=game).exists():
                raise ValidationError("You already added this game.")
            return data


class UserGameDetailSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)

    class Meta:
        model = UserGame
        fields = '__all__'


# 📝 Review Serializer
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    game = GameSerializer(read_only=True)


    class Meta:
        model = Review
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

# 📝 Review Create Serializer
class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['user']

    


