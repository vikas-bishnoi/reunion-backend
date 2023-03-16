from django.conf import settings

from rest_framework import authentication
from rest_framework import exceptions
import jwt

from main.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION')
            if token is None:
                return None
            else:
                bearer, jwt_token = token.split(" ")
                decoded = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=["HS256"])
                pk = decoded.get("id")
                user = User.objects.get(id=id)
                return (user, None)

        except ValueError:
            return None
        
        except jwt.exceptions.DecodeError:
            return exceptions.AuthenticationFailed(detail="JWT Format invalid")
        
        except User.DoesNotExist:
            return exceptions.AuthenticationFailed(detail="User does not exist")