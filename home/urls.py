from django.urls import path, include

# from home import views
import views

app_name = "home"

urlpatterns = [
    path('home/', views.home, name='home'),
]