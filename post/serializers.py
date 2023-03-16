from rest_framework import serializers
from post.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('author', )
    
    def create(self, validated_data):
        author = self.context.get("request").user
        print(author)
        post = Post.objects.create(**validated_data, author=author)
        return post