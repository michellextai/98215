# Django imports
from django import forms
from django.forms import ModelForm

# Model imports
from .models import blog

class BlogPost(ModelForm):
    class Meta:
        model = blog # Use models from blog class
        # fields = ['title', 'context']
        exclude = ['']
