from django.urls import path
from . import views

# Here we are creating our routes, which connects a url to our views which the views connects to the HTML template
# So, we call path, and leave the quotes empty if we plan to specify the path in the main urls.py file, then
# reference the view method and leave an optional name.
# For the second path we added "new" and this is an extension to the original so it looks like ...resume/new,
# which is where I want my users to create their "new" resumes or for management to create "new" vacancies

# app_name is used to reference this file in our form templates using
# {% url 'app_name:view_name' some_argument %}
app_name = "resume_paths"
urlpatterns = [
    path('', views.get_resume, name='resume_list'),
    path("new", views.create_resume_page, name="create_page"),
    path("write", views.create_resume, name="create_resume"),
]
