from django.contrib import admin

from .models import Obstacle, ObstaclePhoto, ObstacleComment, ObstacleCommentPhoto


class ObstaclePhotoInline(admin.TabularInline):
    model = ObstaclePhoto


class ObstacleAdmin(admin.ModelAdmin):
    model = Obstacle
    inlines = [
        ObstaclePhotoInline,
    ]
    list_display = [
        'location',
        'author',
        'type',
        'is_active',
    ]
    list_filter = (
        'is_active',
        'type',
    )
    readonly_fields = ('author', 'location', 'created', 'last_modified')


class ObstacleCommentPhotoInline(admin.TabularInline):
    model = ObstacleCommentPhoto


class ObstacleCommentAdmin(admin.ModelAdmin):
    model = ObstacleComment
    inlines = [
        ObstacleCommentPhotoInline,
    ]
    list_display = [
        'get_obstacle',
        'author',
        'rating',
    ]

    @admin.display(ordering='obstacle__id', description='Obstacle')
    def get_obstacle(self, obj):
        return obj.obstacle.type


admin.site.register(Obstacle, ObstacleAdmin)
admin.site.register(ObstacleComment, ObstacleCommentAdmin)
