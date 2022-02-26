import uuid
from django.db import models
from django.contrib.auth import get_user_model


class Location(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.address or f'{self.latitude} {self.longitude}'


class FavoritePlace(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} : {self.location}'
