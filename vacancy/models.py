from django.db import models
from django.db.models import CharField, ForeignKey
from django.conf import settings

# Same process as resume/models so read the description & summary of how this works there.

class Vacancy(models.Model):
    description = CharField(max_length=1024)
    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
