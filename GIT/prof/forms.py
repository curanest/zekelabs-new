from django import forms
from django.forms import ModelForm
from .models import RegisterProfile 
from django.db import models
from django.contrib.auth.models import User


class Register(forms.ModelForm):
    class Meta:
        model = RegisterProfile
        fields = '__all__'