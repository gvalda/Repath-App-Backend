from dataclasses import fields
from email.policy import default
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


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(max_length=50)

    class Meta:
        fields = (
            'email',
            'username',
            'avatar',
            'is_active',
            'date_joined'
        )
        read_only_fields = (
            'is_active',
            'date_joined',
        )
        model = User


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
    # comments = serializers.HyperlinkedIdentityField(
    #     many=True,
    #     read_only=True,
    #     view_name='comment-detail',
    # )
    photos = ImageUrlField(
        many=True,
        read_only=True,
    )
    author_id = serializers.HiddenField(
        source='author',
        default=serializers.CurrentUserDefault(),
    )
    author = serializers.CharField(source='author.email', read_only=True)
    location = LocationSerializer()

    class Meta:
        fields = (
            'id',
            'location',
            'author_id',
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

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        location = Location.objects.create(**location_data)
        obstacle = Obstacle.objects.create(location=location, **validated_data)
        return obstacle


class ObstacleWithoutLocationSerializer(ObstacleSerializer):
    class Meta(ObstacleSerializer.Meta):
        read_only_fields = (
            'location',
            'is_active',
            'last_modified',
        )


class ObstacleCommentSerializer(serializers.ModelSerializer):
    photos = ImageUrlField(
        many=True,
        read_only=True,
    )
    author_id = serializers.HiddenField(
        source='author',
        default=serializers.CurrentUserDefault(),
    )
    author = serializers.CharField(source='author.email', read_only=True)

    class Meta:
        fields = (
            'id',
            'obstacle',
            'author_id',
            'author',
            'rating',
            'comment',
            'photos',
            'last_modified',
        )
        read_only_fields = (
            'last_modified',
        )
        model = ObstacleComment
