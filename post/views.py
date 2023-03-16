from rest_framework import viewsets
from rest_framework import permissions

from post.models import Post
from post.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [permissions.IsAuthenticated]
        
        return [permission() for permission in permission_classes]
