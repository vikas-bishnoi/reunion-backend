from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from post.models import Post
from post.serializers import PostSerializer
from post.permissions import IsAuthor

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsAuthor]
        
        return [permission() for permission in permission_classes]
    