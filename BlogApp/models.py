
from tkinter import CASCADE
from django.db import models
from django.urls import reverse
# Create your models here.
from datetime import datetime, time
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    cat = Category.objects.all().values_list('name', 'name')

    choice_list = []

    for item in cat:
        choice_list.append(item)
    title = models.CharField(max_length=50)
    title_tag = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length=200, choices=choice_list, default='coding')
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')


# now it will create a model to associate with one to
# to one with the User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    #
    profile_pic = models.ImageField(
        blank=True, null=True, upload_to='images/profile')
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    Instagram_url = models.CharField(max_length=255, null=True, blank=True)
    Twitter_url = models.CharField(max_length=255, null=True, blank=True)
    LinkedIn_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)
