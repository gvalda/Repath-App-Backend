from django.contrib import admin

from .models import Location, FavoritePlace

admin.site.register(Location)
admin.site.register(FavoritePlace)
