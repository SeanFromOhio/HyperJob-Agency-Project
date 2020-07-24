"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from .views import MySignupView, MyLoginView
from django.contrib.auth.views import LogoutView
from resume.views import create_resume_page
from vacancy.views import create_vacancy_page

# This is the main routing area, which controls the flow of the overall website. Things to notice are that
# we have an empty string for out landing page, and then specify all other routes. Include is used to access
# the more local url.py files within each of the app folders.
# Redirect is used to redirect the user to the correct page if they specify the url incorrectly (say an incorrect /)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("landing.urls")),
    path("resumes/", include("resume.urls")),
    path("vacancies/", include("vacancy.urls")),
    path("signup", MySignupView.as_view(), name="signup page"),
    path("login", MyLoginView.as_view(), name="login page"),
    path("signup/", RedirectView.as_view(url="/signup")),
    path("login/", RedirectView.as_view(url="/login")),
    path("home/", include("profile_page.urls")),
    path("logout", LogoutView.as_view()),
    path("resume/new", create_resume_page, name="create_resume_page"),
    path("vacancy/new", create_vacancy_page, name="create_vacancy_page"),
]
