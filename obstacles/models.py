import os
import uuid

from django.contrib.auth import get_user_model
from django.db import models

from locations.models import Location


def get_obstacle_photo_path(instance, filename):
    return os.path.join('obstacles', str(instance.obstacle.id), 'images', filename)


def get_obstacle_comment_photo_path(instance, filename):
    obstacle_comment = instance.obstacle_comment
    return os.path.join(
        'obstacles',
        str(obstacle_comment.obstacle.id),
        'comments',
        str(obstacle_comment.id),
        'images',
        filename
    )


class Obstacle(models.Model):
    class ObstacleType(models.TextChoices):
        Error = 'Error'
        Obstacle = 'Obstacle'
        Pothole = 'Pothole'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        editable=False,
    )
    type = models.CharField(
        max_length=10, choices=ObstacleType.choices, default=ObstacleType.Obstacle
    )
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
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
    obstacle = models.ForeignKey(
        Obstacle, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(
        upload_to=get_obstacle_photo_path,
        default='images/default.jpg'
    )

    def __str__(self):
        return f'{self.obstacle}'


class ObstacleComment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    obstacle = models.ForeignKey(
        Obstacle, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.obstacle} : {self.user} : {self.comment}'


class ObstacleCommentPhoto(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    obstacle_comment = models.ForeignKey(
        ObstacleComment, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(
        upload_to=get_obstacle_comment_photo_path,
        default='images/default.jpg',
        max_length=255
    )

    def __str__(self):
        return f'{self.obstacle_comment}'
