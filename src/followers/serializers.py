from rest_framework import serializers
from src.profiles.serializers import UserByFollowerSerializer, GetUserDevPublicSerializer
from .models import Follower


class ListFollowerSerializer(serializers.ModelSerializer):
    subscriber = UserByFollowerSerializer(read_only=True)

    class Meta:
        model = Follower
        fields = ('subscriber',)


    
