from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

from .models import Game, UserGame, Review
from .serializers import GameSerializer, UserGameSerializer, ReviewSerializer

# CRUD ViewSets
class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class UserGameViewSet(viewsets.ModelViewSet):
    queryset = UserGame.objects.all()
    serializer_class = UserGameSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class GameSearchView(APIView):
    def get(self, request):
        query = request.GET.get('q')
        if not query:
            return Response({"error": "Missing game name (?q=game_name)"}, status=400)

        url = f"https://api.rawg.io/api/games?key=2879074ca318435d949256865979750e&search={query}"
        response = requests.get(url)

        if response.status_code != 200:
            return Response({"error": "Failed to fetch data from RAWG"}, status=500)

        data = response.json()
        results = data.get('results', [])

        filtered = []
        for game in results:
            platforms_data = game.get('platforms')
            platforms_list = []
            if platforms_data:
                platforms_list = [p['platform']['name'] for p in platforms_data if p.get('platform')]

            filtered.append({
                'name': game.get('name'),
                'released': game.get('released'),
                'rating': game.get('rating'),
                'image': game.get('background_image'),
                'platforms': platforms_list
            })

        return Response(filtered)

