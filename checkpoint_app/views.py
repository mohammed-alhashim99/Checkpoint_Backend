from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework.generics import RetrieveAPIView
from rest_framework import generics, permissions, status
from .models import Game, UserGame, Review
from .serializers import (
    GameSerializer, ReviewListSerializer, UserGameCreateSerializer, UserGameDetailSerializer,
    UserSerializer, ReviewSerializer, ReviewCreateSerializer
)
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken



class GameByGameIdDetail(RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = 'game_id'


class GameListCreate(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.AllowAny]

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.AllowAny]


class UserGameListCreate(generics.ListCreateAPIView):
    queryset = UserGame.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserGame.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        return UserGameCreateSerializer
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserGameCreateSerializer  
        return UserGameDetailSerializer

class UserGameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserGame.objects.all()
    serializer_class = UserGameCreateSerializer
    permission_classes = [IsAuthenticated]

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [permissions.AllowAny()] 

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ReviewCreateSerializer
        return ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return ReviewCreateSerializer
        return ReviewSerializer
    
class ReivewGamesList(generics.ListAPIView):
    queryset = Review.objects.all().distinct("game")
    serializer_class = ReviewListSerializer
    permission_classes = [permissions.AllowAny]


class ReviewByGameIdList(generics.ListAPIView):
    serializer_class = ReviewListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        game_id = self.kwargs['game_id']
        return Review.objects.filter(game__game_id=game_id)





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
                    "game_id":game.get("id"),
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
