from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader

# Create your views here.
# In Django, web pages and other content are delivered by views. 
# Each view is represented by a Python function (or method, 
# in the case of class-based views). Django will choose a view 
# by examining the URL that’s requested (to be precise, 
# the part of the URL after the domain name).

# To get from a URL to a view, Django uses what are known as ‘URLconfs’. 
# A URLconf maps URL patterns to views

# Each view is responsible for doing one of two things: 
# returning an HttpResponse object containing the content 
# for the requested page, or raising an exception such as Http404. 
# The rest is up to you.

# All Django wants is that HttpResponse. Or an exception

def index(request):
    # That code loads the template called polls/index.html and 
    # passes it a context. The context is a dictionary mapping 
    # template variable names to Python objects.

    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # It’s a very common idiom to load a template, fill a context 
    # and return an HttpResponse object with the result of the 
    # rendered template:
    #template = loader.get_template("polls/index.html")
    #context = {"latest_question_list": latest_question_list}
    #return HttpResponse(template.render(context, request))

    # Django provides a shortcut
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
    


def detail(request, question_id):
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    # Shortcut for the above code:
    question = get_object_or_404(Question, pk=question_id)
    # The get_object_or_404() function takes a Django model as 
    # its first argument and an arbitrary number of keyword arguments, 
    # which it passes to the get() function of the model’s manager. 
    # It raises Http404 if the object doesn’t exist.
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


