from django.urls import path
from . import views

app_name = "profile_paths"
urlpatterns = [
    path('', views.get_profile, name='profile_page'),
]
