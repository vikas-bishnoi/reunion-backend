from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("authenticate/", views.login),
    path("user/", views.UserView.as_view()),
    path("register/", views.RegisterUserView.as_view()),
    path("follow/<int:pk>/", views.FollowView.as_view()),
    path("unfollow/<int:pk>/", views.UnfollowView.as_view()),
]