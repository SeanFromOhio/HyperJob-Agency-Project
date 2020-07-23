from django.db import models
from django.db.models import CharField, ForeignKey
from django.conf import settings

# This is where we create out tables that will house all of the data the either we supply or the consumer supplies
# First, we create a class that inherits from Django's Model class, and then we define our fields below.
# Each field can be thought of as a column, so we have a description column and an author column, as well as
# a primary key field that is default and not needed to be listed here.
# For each field we list the type (CharField or models.CharField if not importing like above) and other constraints.
# Author is utilizing a ForeignKey from the Auth_User_Model and will delete itself if we delete the user from the
# Auth model...
# Lastly, we specified a class string method to list the "description" rather than an object-position (weird text)
# whenever we call upon the model class.

# TLDR: Creates a data table with specified fields utilizing (inherently) Djangos Model table


class Resume(models.Model):
    description = CharField(max_length=1024)
    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
