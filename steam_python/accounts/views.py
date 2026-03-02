from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
#para agregar campos "first_name", "last_name" y "email" al registrarse
from .forms import CustomUserCreationForm 


class SignUpView(CreateView):
    form_class = CustomUserCreationForm 
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


