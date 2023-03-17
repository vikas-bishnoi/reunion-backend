from django.urls import path
from post import views

from rest_framework.routers import DefaultRouter

app_name = "post"

router = DefaultRouter()
router.register("posts", views.PostViewSet)

urlpatterns = [
    path("comment/<int:pk>", views.CommentView.as_view(), name="comment"),
    path("like/<int:pk>", views.LikeView.as_view(), name="like"),
    path("unlike/<int:pk>", views.UnlikeView.as_view(), name="unlike"),
    path("all_posts", views.PostViewSet.as_view({'get': 'list'}), name="all_posts"),
]

urlpatterns += router.urls
