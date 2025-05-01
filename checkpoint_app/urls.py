from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, UserGameViewSet, ReviewViewSet, GameSearchView

router = DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'usergames', UserGameViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/', GameSearchView.as_view(), name='game-search'),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, UserGameViewSet, ReviewViewSet, GameSearchView

router = DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'usergames', UserGameViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/', GameSearchView.as_view(), name='game-search'),
]
