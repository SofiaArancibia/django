from django.contrib import admin
from .models import Question
# Register your models here.

# Now that we’ve registered Question, 
# Django knows that it should be displayed on the admin index page
admin.site.register(Question)