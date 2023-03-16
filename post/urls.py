from django.urls import path
from post import views

# from rest_framework.routers import DefaultRouter

app_name = "post"

# router = DefaultRouter()
# router.register("posts", views.PostViewSet)

urlpatterns = [
    path("authenticate/", views.PostViewSet.as_view({'get': 'list'})),
]