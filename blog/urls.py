from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/new/', views.post_new, name='post_new'),
    path('posts/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('accounts/login/', views.user_login_view, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('', include('django.contrib.auth.urls')),
    path('register_user', views.user_register, name='user_register'),
]
