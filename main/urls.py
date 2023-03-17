from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("authenticate/", views.login, name='authenticate'),
    path("user/", views.UserView.as_view(), name='user'),
    path("register/", views.RegisterUserView.as_view(), name='register'),
    path("follow/<int:pk>/", views.FollowView.as_view(), name='follow'),
    path("unfollow/<int:pk>/", views.UnfollowView.as_view(), name='unfollow'),
]