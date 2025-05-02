from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import Game, UserGame, Review
from .serializers import GameSerializer, UserGameSerializer, ReviewSerializer
import requests


def home_view(request):
    return JsonResponse({'message': 'Welcome to the Game API'})

## 🕹️ Game Views
class GameListCreate(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.AllowAny]

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.AllowAny]

## 👤 UserGame Views
class UserGameListCreate(generics.ListCreateAPIView):
    queryset = UserGame.objects.all()
    serializer_class = UserGameSerializer
    permission_classes = [permissions.AllowAny]

class UserGameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserGame.objects.all()
    serializer_class = UserGameSerializer
    permission_classes = [permissions.AllowAny]

## 📝 Review Views
class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]  # لاحقًا: IsAuthenticated

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

## 🔍 Game Search via RAWG API
class GameSearchView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        query = request.GET.get('q')
        if not query:
            return Response({"error": "Missing game name (?q=game_name)"}, status=400)

        try:
            url = f"https://api.rawg.io/api/games?key=2879074ca318435d949256865979750e&search={query}"
            response = requests.get(url)

            if response.status_code != 200:
                return Response({"error": "Failed to fetch from RAWG"}, status=response.status_code)

            data = response.json().get('results', [])
            filtered = []

            for game in data:
                platforms = [p['platform']['name'] for p in game.get('platforms', []) if p.get('platform')]
                filtered.append({
                    'image': game.get('background_image'),
                    'name': game.get('name'),
                    'released': game.get('released'),
                    'rating': game.get('rating'),
                    'image': game.get('background_image'),
                    'platforms': platforms
                })

            return Response(filtered)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
