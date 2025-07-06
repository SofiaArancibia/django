from django.urls import path

from . import views


# since you defined the name argument in the path() functions 
# you can remove a reliance on specific URL paths defined in 
# your url configurations by using the {% url %} template tag
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]