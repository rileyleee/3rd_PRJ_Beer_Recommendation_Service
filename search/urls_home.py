from django.urls import path
from search import views

urlpatterns = [
    path('home/', views.homepage),
    path('home/ranking', views.recommend),
]

