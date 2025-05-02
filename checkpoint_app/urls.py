from django.urls import path
from .views import (
    GameListCreate, GameDetail,
    UserGameListCreate, UserGameDetail,
    ReviewListCreate, ReviewDetail,
    GameSearchView, home_view
)

urlpatterns = [
    path('', home_view),
    # 🎮 Game
    path('games/', GameListCreate.as_view()),
    path('games/<int:pk>/', GameDetail.as_view()),

    # 👤 UserGame
    path('usergames/', UserGameListCreate.as_view()),
    path('usergames/<int:pk>/', UserGameDetail.as_view()),

    # 📝 Review
    path('reviews/', ReviewListCreate.as_view()),
    path('reviews/<int:pk>/', ReviewDetail.as_view()),

    # 🔍 RAWG Search
    path('search/', GameSearchView.as_view()),
]
