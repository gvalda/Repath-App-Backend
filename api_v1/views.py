from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from locations.models import Location, FavoritePlace
from obstacles.models import (
    Obstacle,
    UserObstacleComment,
)

from .serializers import (
    LocationSerializer,
    FavoritePlaceSerializer,
    ObstacleSerializer,
    UserObstacleCommentSerializer,
)
from .permissions import IsUserAuthor


class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class FavoritePlaceList(generics.ListCreateAPIView):
    queryset = FavoritePlace.objects.all()
    serializer_class = FavoritePlaceSerializer
    permission_classes = (
        IsAuthenticated,
    )

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class FavoritePlaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FavoritePlace.objects.all()
    serializer_class = FavoritePlaceSerializer
    permission_classes = (
        IsAuthenticated,
        IsAdminUser | IsUserAuthor
    )


class ObstacleList(generics.ListCreateAPIView):
    queryset = Obstacle.objects.all()
    serializer_class = ObstacleSerializer


class ObstacleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Obstacle.objects.all()
    serializer_class = ObstacleSerializer


class UserObstacleCommentList(generics.ListCreateAPIView):
    queryset = UserObstacleComment.objects.all()
    serializer_class = UserObstacleCommentSerializer
    filter_backends = (DjangoFilterBackend,)
    search_fields = ['obstacle']


class UserObstacleCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserObstacleComment.objects.all()
    serializer_class = UserObstacleCommentSerializer
    filter_backends = (DjangoFilterBackend,)
    search_fields = ['obstacle', 'pk']
