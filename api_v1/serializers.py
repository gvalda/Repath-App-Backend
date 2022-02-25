from rest_framework import serializers

from locations.models import Location, FavoritePlace
from obstacles.models import (
    Obstacle,
    ObstaclePhoto,
    UserObstacleComment,
    UserObstacleCommentPhoto,
)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'latitude',
            'longitude',
            'address',
        )
        model = Location


class FavoritePlaceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'location',
            'user',
            'last_modified',
        )
        read_only_fields = (
            'last_modified',
        )
        model = FavoritePlace


class ObstacleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'location',
            'author',
            'type',
            'description',
            'is_active',
            'last_modified',
        )
        read_only_fields = (
            'is_active',
            'last_modified',
        )
        model = Obstacle


class UserObstacleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'obstacle',
            'user',
            'rating',
            'comment',
            'last_modified',
        )
        read_only_fields = (
            'last_modified',
        )
        model = UserObstacleComment
