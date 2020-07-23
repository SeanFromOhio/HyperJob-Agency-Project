from .models import Vacancy
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.models import User


def get_vacancy(request, *args, **kwargs):
    vacancy_list = Vacancy.objects.all()
    context = {"vacancy_list": vacancy_list}
    return render(request, "vacancy/vacancy_list.html", context)


def create_vacancy_page(request):
    if request.user.is_superuser:
        return render(request, "vacancy/vacancy_create.html", {})
    else:
        return HttpResponseForbidden()


def create_vacancy(request):
    if request.user.is_superuser:
        vacancy_description = request.POST.get("vacancy_description")
        vacancy_author = request.user.username
    else:
        return HttpResponseForbidden()

    vacancy_model = Vacancy()
    vacancy_model.description = vacancy_description
    vacancy_model.author = User.objects.get(username=vacancy_author)
    vacancy_model.save()

    return HttpResponseRedirect(reverse("profile_paths:profile_page"))
