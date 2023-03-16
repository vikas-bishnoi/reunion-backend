from django.contrib.auth import authenticate
from django.conf import settings

import jwt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from main.serializers import UserSerializer


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
    def get(self, request):
        if request.user.is_authenticated:
            user = UserSerializer(request.user)
            return Response(data=user.data)
