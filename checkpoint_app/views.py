from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework import generics, permissions,status
from .models import Game, UserGame, Review
from .serializers import GameSerializer, UserGameSerializer, ReviewSerializer , UserGameCreateSerializer, UserGameDetailSerializer,UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# 🕹️ Game Views
class GameListCreate(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.AllowAny]

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.AllowAny]

# 👤 UserGame Views
class UserGameListCreate(generics.ListCreateAPIView):
    queryset = UserGame.objects.all()
    serializer_class = UserGameSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        # print('🔎 Incoming request:', request.data) 
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print('❌ Errors:', serializer.errors)
            return Response(serializer.errors, status=400)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)
    
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserGameCreateSerializer
        return UserGameDetailSerializer


class UserGameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserGame.objects.all()
    serializer_class = UserGameSerializer
    permission_classes = [permissions.AllowAny]

# 📝 Review Views
class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]


class GameSearchView(APIView):
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
            results = []

            for game in data:
                platforms = [p['platform']['name'] for p in game.get('platforms', [])]
                results.append({
                    "name": game.get("name"),
                    "released": game.get("released"),
                    "rating": game.get("rating"),
                    "platforms": platforms,
                    "image": game.get("background_image")

                })
            return Response(results)

        except Exception as e:
            return Response({"error": str(e)}, status=500)


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': response.data
        }, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password')
        )
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            })
        return Response({'error': 'Invalid credentials'}, status=401)