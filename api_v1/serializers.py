from rest_framework import serializers

from locations.models import Location, FavoritePlace
from obstacles.models import (
    Obstacle,
    ObstaclePhoto,
    ObstacleComment,
    ObstacleCommentPhoto,
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


class ImageUrlField(serializers.RelatedField):
    def to_representation(self, instance):
        url = instance.photo.url
        request = self.context.get('request', None)
        if request is not None:
            return request.build_absolute_uri(url)
        return url


class ObstacleSerializer(serializers.ModelSerializer):
    comments = serializers.HyperlinkedIdentityField(
        many=True,
        read_only=True,
        view_name='user-comment-detail',
    )
    photos = ImageUrlField(
        many=True,
        read_only=True,
    )

    class Meta:
        fields = (
            'id',
            'location',
            'author',
            'type',
            'description',
            'comments',
            'photos',
            'is_active',
            'last_modified',
        )
        read_only_fields = (
            'is_active',
            'last_modified',
        )
        model = Obstacle


class ObstacleCommentSerializer(serializers.ModelSerializer):
    photos = ImageUrlField(
        many=True,
        read_only=True,
    )

    class Meta:
        fields = (
            'id',
            'obstacle',
            'user',
            'rating',
            'comment',
            'photos',
            'last_modified',
        )
        read_only_fields = (
            'last_modified',
        )
        model = ObstacleComment
