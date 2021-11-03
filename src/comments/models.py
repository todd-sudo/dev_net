from django.db import models
from django.db.models.deletion import RESTRICT
from django.db.models.expressions import F
from mptt.fields import TreeForeignKey


class AbstractComment(models.Model):
    """ Абстрактная модель комментариев
    """
    text = models.TextField("Текст", max_length=512)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    update_date = models.DateTimeField("Дата обновления", auto_now=True)
    published = models.BooleanField("Опубликовать?", default=True)
    deleted = models.BooleanField("Удаленный статус", default=False)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        abstract = True

