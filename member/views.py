from cProfile import Profile
from re import template
from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView

from .forms import ApnaPasswordCondition, EditProfileForm, SignUpForm


# for profile details views
# usKe liye DetailView ka use kiye hai
class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'file/profile.html'


class PasswordChange(PasswordChangeView):
    form_class = ApnaPasswordCondition
    success_url = reverse_lazy('password-change')


def PasswordMessage(request):
    return render(request, 'passwordchange2.html', {})


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'file/register.html'
    success_url = reverse_lazy('login')


class UserEditPage(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'editprofile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
