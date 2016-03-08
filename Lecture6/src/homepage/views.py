# Default imports
from django.shortcuts import render
from .models import *

from .forms import *

# Authentication imports
from django.contrib.auth import authenticate, login, logout
from helloworld import settings # settings.py
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    all_object = blog.objects.all()
    zero_object = all_object[0]
    first_object = all_object[1]
    zero_object_title = zero_object.title
    form = BlogPost(request.POST or None) # This is our Form

    # Save
    if form.is_valid():
        var = form.save(commit = 'false')
        var.save()

    template = "home.html"
    context = {
    "form" : form,
    "all_object" : all_object,
    "zero_object" : zero_object,
    "first_object" : first_object,
    "zero_object_title" : zero_object_title,
    }
    return render(request, template, context)