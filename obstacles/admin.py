from django.contrib import admin

from .models import Obstacle, ObstaclePhoto, UserObstacleComment, UserObstacleCommentPhoto

admin.site.register(Obstacle)
admin.site.register(ObstaclePhoto)
admin.site.register(UserObstacleComment)
admin.site.register(UserObstacleCommentPhoto)
