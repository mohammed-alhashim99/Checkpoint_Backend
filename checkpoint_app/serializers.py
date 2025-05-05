from rest_framework import serializers
from .models import Game, UserGame, Review
from django.contrib.auth.models import User

# 🎮 Game Serializer
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

# ✅ UserGame Serializer (يمنع التكرار)
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

# ✅ UserGame Detail Serializer (للعرض مع تفاصيل اللعبة)
class UserGameDetailSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)

    class Meta:
        model = UserGame
        fields = '__all__'

# 👤 User Serializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

# 📝 Review Serializer
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    game = GameSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

# 📝 Review Create Serializer
class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['user']
