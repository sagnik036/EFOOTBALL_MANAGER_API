from rest_framework import serializers
from .models import *


class UserSerializer(serializers.Serializer):
    class Meta:
        model=CustomUser
        fields=['mobile','password','team_name','pes_id']