from django.urls import path
from search import views

urlpatterns = [
     path('', views.search),
     path('recommend/', views.recommend),
     path('list/', views.search_list),
     path('beerprofile/<int:pk>/', views.search_detail),
    ]

    