from django.shortcuts import render
from .models import Resume
from django.urls import reverse
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.models import User


# Get resumes and display them
def get_resume(request, *args, **kwargs):
    resume_list = Resume.objects.all()
    context = {"resume_list": resume_list}
    return render(request, "resume/resume_list.html", context)


# Resume creation screen
def create_resume_page(request, *args, **kwargs):
    if request.user.is_authenticated:
        return render(request, "resume/resume_create.html", {})
    else:
        return HttpResponseForbidden()


# Accesses html form and puts the data into the Resume DB
def create_resume(request):
    if request.user.username:
        resume_author = request.user.username
        resume_description = request.POST.get("resume_description")
    else:
        return HttpResponseForbidden()

    resume = Resume()
    resume.description = resume_description
    resume.author = User.objects.get(username=resume_author)
    resume.save()

    return HttpResponseRedirect(reverse("profile_paths:profile_page"))
