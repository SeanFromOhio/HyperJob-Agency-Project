from django.urls import path
from . import views

# Description in resume/urls.py

app_name = "vacancy_paths"
urlpatterns = [
    path('', views.get_vacancy, name='vacancy_list'),
    path("write", views.create_vacancy, name="create_vacancy"),
]
