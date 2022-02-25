from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics

from locations.models import Location, FavoritePlace
from obstacles.models import (
    Obstacle,
    ObstacleComment,
)

from .serializers import (
    LocationSerializer,
    FavoritePlaceSerializer,
    ObstacleSerializer,
    ObstacleCommentSerializer,
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
    queryset = ObstacleComment.objects.all()
    serializer_class = ObstacleCommentSerializer


class UserObstacleCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ObstacleComment.objects.all()
    serializer_class = ObstacleCommentSerializer
