from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView

from post.models import Post
from post.serializers import PostSerializer, PostListDetailSerializer, PostDetailSerializer
from post.permissions import IsAuthor


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return PostSerializer
        elif self.action == 'list':
            return PostListDetailSerializer
        return PostDetailSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsAuthor]
        
        return [permission() for permission in permission_classes]


class CommentView(APIView):
    pass