from django.db import models
from django.conf import settings
from django.db.models.fields import PositiveIntegerField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from src.comments.models import AbstractComment


class Post(models.Model):
    """ Модель поста
    """
    text = models.TextField("Текст", max_length=1024)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    published = models.BooleanField("Опубликовано?", default=True)
    moderation = models.BooleanField("Модерация", default=True)
    view_count = models.PositiveIntegerField("Кол-во просмотров", default=0)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )

    def __str__(self) -> str:
        return f"{self.id}"

    def comments_count(self):
        return self.comments.count()

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(AbstractComment, MPTTModel):
    """ Модель комментариев
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children"
    )

    def __str__(self) -> str:
        return f"{self.user} - {self.post}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
