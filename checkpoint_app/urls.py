from django.urls import path
from .views import (
    GameListCreate, GameDetail, GameSearchView,
    UserGameListCreate, UserGameDetail,
    ReviewListCreate, ReviewDetail
)

urlpatterns = [
    # 🎮 Games
    path('games/', GameListCreate.as_view()),
    path('games/<int:pk>/', GameDetail.as_view()),

    # 👤 UserGames
    path('usergames/', UserGameListCreate.as_view()),
    path('usergames/<int:pk>/', UserGameDetail.as_view()),

    # 📝 Reviews
    path('reviews/', ReviewListCreate.as_view()),
    path('reviews/<int:pk>/', ReviewDetail.as_view()),

    path('search/', GameSearchView.as_view()), 
]
