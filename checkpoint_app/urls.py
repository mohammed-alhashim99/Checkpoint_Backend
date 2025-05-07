from django.urls import path
from .views import (
    GameByGameIdDetail, GameListCreate, GameDetail, GameSearchView, LoginView, ReviewByGameIdList, SignupView,
    UserGameListCreate, UserGameDetail,
    ReviewListCreate, ReviewDetail,ReivewGamesList
)

urlpatterns = [
    
    path('games/', GameListCreate.as_view()),
    path('games/<int:pk>/', GameDetail.as_view()),
    path('games/by-game-id/<int:game_id>/', GameByGameIdDetail.as_view()),


    
    path('usergames/', UserGameListCreate.as_view()),
    path('usergames/<int:pk>/', UserGameDetail.as_view()),

    
    path('reviews/', ReviewListCreate.as_view()),
    path('reviews/<int:pk>/', ReviewDetail.as_view()),
    path('reviews/games/', ReivewGamesList.as_view()),
    path('reviews/by-game/<int:game_id>/', ReviewByGameIdList.as_view()),



    path('search/', GameSearchView.as_view()), 

    path('users/signup/', SignupView.as_view(), name='signup'),
    path('users/login/', LoginView.as_view(), name='login'),
]
