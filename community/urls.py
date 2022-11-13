from django.urls import path
from community import views

urlpatterns = [
    path('column/', views.column),
    path('column/new/', views.column_new),
   # path('column/<int:pk>/', views.column_detail),
    path('event/', views.event_index),
    path('event/new/', views.event_new),
   # path('event/<int:pk>/', views.event_detail),
]

