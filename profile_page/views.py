from django.shortcuts import render
from resume.models import Resume
from vacancy.models import Vacancy


def get_profile(request, *args, **kwargs):
    current_author_id = request.user.id
    resume_lst = Resume.objects.filter(author=current_author_id)
    vacancy_lst = Vacancy.objects.filter(author=current_author_id)

    context = {
        "resume_lst": resume_lst,
        "vacancy_lst": vacancy_lst,
    }

    return render(request, "profile_page/profile_page.html", context)
