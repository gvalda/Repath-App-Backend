from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from rest_framework import serializers

from locations.models import Location, FavoritePlace
from obstacles.models import (
    Obstacle,
    ObstacleComment,
)


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password',
        )

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


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
        view_name='comment-detail',
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
