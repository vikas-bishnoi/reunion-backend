from django.urls import path
from post import views

from rest_framework.routers import DefaultRouter

app_name = "post"

router = DefaultRouter()
router.register("", views.PostViewSet)

urlpatterns = router.urls
