from django.urls import path
from search import views

urlpatterns = [    
    path('', views.index),
    path('<int:pk>/', views.single_post_page), # 몇번째 글이든 불러올 수 있도록 모든 숫자를 가져올 수 있도록 <int>로 입력
    path('new/', views.post_new),
    path('restaurant/', views.restaurant),
    path('restaurant/<int:pk>/', views.single_restaurant_page),
    path('restaurant/new/', views.restaurant_new),
    ]

    