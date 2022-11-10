from django.urls import path
from account import views

urlpatterns = [
    path("login/", views.login),
    path("logout/", views.logout),
    path("signup/", views.signup),
    path("mypage/", views.mypage),
    path("mybeer/", views.mybeer),
]