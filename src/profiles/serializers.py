from rest_framework import serializers
from .models import UserDev


class GetUserDevSerializer(serializers.ModelSerializer):
    """ Вывод инфо о user
    """
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserDev
        exclude = (
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        )


class GetUserDevPublicSerializer(serializers.ModelSerializer):
    """ Вывод публичной инфы о user
    """
    class Meta:
        model = UserDev
        exclude = (
            "email",
            "phone",
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        )


class UserByFollowerSerializer(serializers.ModelSerializer):
    """ Сериализация для подписчиков
    """
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserDev
        fields = ('id', 'username', 'avatar')