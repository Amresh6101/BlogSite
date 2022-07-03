from django import views
from django.urls import path
from .views import UserEditPage, UserRegisterView, PasswordChange
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('editprofile/', UserEditPage.as_view(), name="edit-profile"),
    path('password/', PasswordChange.as_view(template_name="passwordchange.html")),
    path('passwordchange/', views.PasswordMessage, name="password-change"),

]
