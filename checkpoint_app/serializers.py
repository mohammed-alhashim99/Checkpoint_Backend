from rest_framework import serializers
from .models import Game, UserGame, Review

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

class UserGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGame
        fields = '__all__'

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
