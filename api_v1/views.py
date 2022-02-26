from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import generics

from locations.models import Location, FavoritePlace
from obstacles.models import (
    Obstacle,
    ObstacleComment,
)

from .serializers import (
    RegisterSerializer,
    UserSerializer,
    LocationSerializer,
    FavoritePlaceSerializer,
    ObstacleSerializer,
    ObstacleWithoutLocationSerializer,
    ObstacleCommentSerializer,
)
from .permissions import IsUserAuthor, IsAuthorOrReadOnly


User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'email'


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
        IsAdminUser | IsUserAuthor,
    )


class ObstacleList(generics.ListCreateAPIView):
    queryset = Obstacle.objects.all()
    serializer_class = ObstacleSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
    )


class ObstacleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Obstacle.objects.all()
    serializer_class = ObstacleSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsAdminUser | IsAuthorOrReadOnly,
    )

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return ObstacleWithoutLocationSerializer
        return ObstacleSerializer


class UserObstacleCommentList(generics.ListCreateAPIView):
    queryset = ObstacleComment.objects.all()
    serializer_class = ObstacleCommentSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
    )


class UserObstacleCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ObstacleComment.objects.all()
    serializer_class = ObstacleCommentSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsAdminUser | IsAuthorOrReadOnly,
    )
