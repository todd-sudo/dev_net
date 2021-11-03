from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import UserDev
from .serializers import GetUserDevSerializer, GetUserDevPublicSerializer


class UserDevPublicView(ModelViewSet):
    """ Вывод публичного профиля пользователя
    """
    queryset = UserDev.objects.all()
    serializer_class = GetUserDevPublicSerializer
    permission_classes = [permissions.AllowAny]


class UserDevView(ModelViewSet):
    """ Вывод профиля пользователя
    """
    serializer_class = GetUserDevSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserDev.objects.filter(id=self.request.user.id)