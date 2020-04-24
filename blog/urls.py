from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/new/', views.post_new, name='post_new'),
    path('posts/<int:pk>/edit', views.post_edit, name='post_edit'),
    ]
