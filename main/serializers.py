from rest_framework import serializers
from main.models import User

class UserSerializer(serializers.ModelSerializer):
    folowers = serializers.ReadOnlyField(
        source='followers.count', 
    )
    following = serializers.ReadOnlyField(
        source='following.count', 
    )
    class Meta:
        model = User
        fields = (
            "name", 
            'folowers',
            'following'
        )