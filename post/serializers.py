from rest_framework import serializers
from post.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('author', )
    
    def create(self, validated_data):
        author = self.context.get("request").user
        post = Post.objects.create(**validated_data, author=author)
        return post

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', )


class PostListDetailSerializer(serializers.ModelSerializer):
    likes = serializers.ReadOnlyField(
        source='liked_by.count', 
    )
    comments = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Post
        exclude = ('author', 'liked_by')
