
from django import forms
from .models import Category, Post
from django.forms import ModelForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author',  'category', 'body', 'image')
