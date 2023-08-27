from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register_success/', views.register_success, name='register_success'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
]
