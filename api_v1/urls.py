from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
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
    path('locations/', LocationList.as_view(), name='location_list'),
    path('locations/<uuid:pk>/',
         LocationDetail.as_view(), name='location_detail'),
    path('obstacles/', ObstacleList.as_view(), name='obstacle_list'),
    path('obstacles/<uuid:pk>/',
         ObstacleDetail.as_view(), name='obstacle_detail'),
    path('obstacles/<uuid:obstacle>/comments/',
         UserObstacleCommentList.as_view(), name='user_comment_list'),
    path('obstacles/<uuid:obstacle>/comments/<uuid:pk>/',
         UserObstacleCommentDetail.as_view(), name='user_comment_detail'),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/favorites/', FavoritePlaceList.as_view(),
         name='user_favorite_place_list'),
    path('users/favorites/<uuid:pk>/', FavoritePlaceDetail.as_view(),
         name='user_favorite_place_detail'),
]
