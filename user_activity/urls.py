from django.urls import path, include

from . import views

app_name = "user_activity"

urlpatterns = [
    path('upload/', views.upload_data, name='upload'),
]