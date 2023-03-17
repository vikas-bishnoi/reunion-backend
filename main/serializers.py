from rest_framework import serializers
from main.models import User

class ReadUserSerializer(serializers.ModelSerializer):
    followers = serializers.ReadOnlyField(
        source='followers.count', 
    )
    following = serializers.ReadOnlyField(
        source='following.count', 
    )
    class Meta:
        model = User
        fields = (
            "name", 
            'followers',
            'following'
        )

class WriteUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "name", 
            "email", 
            "password"
        )
    
    def create(self, validated_data):
        password = validated_data.get('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user