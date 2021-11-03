from django.db import models

from django.conf import settings


class Follower(models.Model):
    """ Модель подписчиков
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='owner'
    )
    subscriber = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='subscribers'
    )

    def __str__(self):
        return f"{self.subscriber} подписан на {self.user}"

    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"
