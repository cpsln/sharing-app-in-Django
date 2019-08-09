from django.urls import path, include
from django.contrib import auth as auth_views

from . import views

app_name = "authman"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path('login/', views.login_view, name="login", ),
    path('logout/', views.logout_view, name="logout"),
]

