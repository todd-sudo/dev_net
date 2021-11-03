from django.contrib import admin

from . import models


@admin.register(models.Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "subscriber")
