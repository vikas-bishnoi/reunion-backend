from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.conf import settings

import jwt

from rest_framework import status
from rest_framework import permissions

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from main.serializers import UserSerializer

from .models import User

@api_view(["POST"])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    if not email or not password:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(email=email, password=password)
    if user:
        encoded_jwt = jwt.encode(
            {"id": user.pk},
            settings.SECRET_KEY,
            algorithm="HS256"
        )
        return Response(data={"token": encoded_jwt}, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
            user = UserSerializer(request.user)
            return Response(data=user.data)


class FollowView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        if pk is not None:
            try:
                current_user = request.user
                following = get_object_or_404(User, pk=pk)
                if current_user != following and current_user not in following.followers.all():
                    following.followers.add(current_user)
                return Response(status=status.HTTP_200_OK)
            except User.DoesNotExist:
                pass
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UnfollowView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        if pk is not None:
            try:
                current_user = request.user
                following = get_object_or_404(User, pk=pk)
                if current_user != following and current_user in following.followers.all():
                    following.followers.remove(current_user)
                return Response(status=status.HTTP_200_OK)
            except User.DoesNotExist:
                pass
        return Response(status=status.HTTP_400_BAD_REQUEST)