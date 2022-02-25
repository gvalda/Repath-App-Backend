from django.urls import path
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
]
