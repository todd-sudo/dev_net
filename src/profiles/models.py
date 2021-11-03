from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import TextField


class UserDev(AbstractUser):
    """ Модель кастомного пользователя
    """
    middle_name = models.CharField("Второе имя", max_length=50)
    avatar = models.ImageField(
        "Аватар", upload_to='user/avatar', null=True, blank=True
    )
    first_login = models.DateTimeField("Первый вход", blank=True, null=True)
    phone = models.CharField("Номер телефона", max_length=14)
    bio = models.TextField(
        "Биография", max_length=5000, blank=True, null=True
    )
    github = models.URLField(
        "GitHub", max_length=512, blank=True, null=True
    )
    technology = models.ManyToManyField(
        "Technology", related_name="users", verbose_name="Технологии", blank=True
    )

    def __str__(self) -> str:
        return f"{self.username}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Technology(models.Model):
    """ Модель технологии
    """
    name = models.CharField("Название технологии", max_length=200)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Технология"
        verbose_name_plural = "Технологии"
