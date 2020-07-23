from django.contrib import admin

from .models import Resume

# Here we are registering our models, meaning that we can access them within the admin page of our website
# From there, we are able to manipulate the data manually.
# The admin.site code is simply changing the wording on the page from "Django Admin" to whatever we specify,
# as well as the site title, and some introductory text for those logging into the admin area

admin.site.site_header = "HyperJob Agency Admin"
admin.site.site_title = "HyperJob Admin Area"
admin.site.index_title = "Welcome to the HyperJob admin area"

admin.site.register(Resume)
