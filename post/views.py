from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from post.models import Post
from post.serializers import PostSerializer, PostListDetailSerializer, PostDetailSerializer, CommentSerializer
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
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        data = {'post': post, 'comment': pk, 'author': request.user}
        serializer = CommentSerializer(data=data)
        # if serializer.is_valid():
        #     vote = serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)