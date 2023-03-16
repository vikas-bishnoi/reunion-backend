from django.urls import path
from post import views

from rest_framework.routers import DefaultRouter

app_name = "post"

router = DefaultRouter()
router.register("posts", views.PostViewSet)

urlpatterns = [
    path("comment/<int:pk>", views.CommentView.as_view(), name="comment"),

]
urlpatterns += router.urls
