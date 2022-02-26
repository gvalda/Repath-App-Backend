from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    RegisterView,
    LocationList,
    LocationDetail,
    FavoritePlaceList,
    FavoritePlaceDetail,
    ObstacleList,
    ObstacleDetail,
    UserObstacleCommentList,
    UserObstacleCommentDetail,
)

urlpatterns = [
    path('locations/', LocationList.as_view(), name='location-list'),
    path('locations/<uuid:pk>/',
         LocationDetail.as_view(), name='location-detail'),
    path('obstacles/', ObstacleList.as_view(), name='obstacle-list'),
    path('obstacles/<uuid:pk>/',
         ObstacleDetail.as_view(), name='obstacle-detail'),
    path('comments/',
         UserObstacleCommentList.as_view(), name='comment-list'),
    path('comments/<uuid:pk>/',
         UserObstacleCommentDetail.as_view(), name='comment-detail'),
    path('users/', RegisterView.as_view(), name='auth-register'),
    path('users/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('users/favorites/', FavoritePlaceList.as_view(),
         name='user-favorite-place-list'),
    path('users/favorites/<uuid:pk>/', FavoritePlaceDetail.as_view(),
         name='user-favorite-place-detail'),
]
