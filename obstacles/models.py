import os
import uuid
from django.db import models
from django.contrib.auth import get_user_model
from locations.models import Location


def get_obstacle_photo_path(instance, filename):
    return os.path.join('obstacles', instance.obstacle.id, 'images', filename)


def get_obstacle_comment_photo_path(instance, filename):
    return os.path.join('obstacles', instance.user_obstacle_comment.obstacle.id, 'comments', instance.user_obstacle_comment.id, 'images', filename)


class Obstacle(models.Model):
    class ObstacleType(models.TextChoices):
        Error = '-1' 'Error'
        Pothole = '0' 'Pothole'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True)
    type = models.CharField(
        max_length=10, choices=ObstacleType.choices, default=ObstacleType.Error
    )
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.created} : {self.location} : {self.author}'


class ObstaclePhoto(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    obstacle = models.ForeignKey(Obstacle, on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to=get_obstacle_photo_path,
        default='images/default.jpg'
    )

    def __str__(self):
        return f'{self.obstacle}'


class UserObstacleComment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    obstacle = models.ForeignKey(Obstacle, on_delete=models.CASCADE)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.obstacle} : {self.user} : {self.comment}'


class UserObstacleCommentPhoto(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    user_obstacle_comment = models.ForeignKey(
        UserObstacleComment, on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to=get_obstacle_comment_photo_path,
        default='images/default.jpg'
    )

    def __str__(self):
        return f'{self.user_obstacle_comment}'
