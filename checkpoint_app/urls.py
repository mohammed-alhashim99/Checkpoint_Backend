from django.urls import path
from .views import (
    GameListCreate, GameDetail, GameSearchView, LoginView, SignupView,
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

    path('users/signup/', SignupView.as_view(), name='signup'),
    path('users/login/', LoginView.as_view(), name='login'),
]
