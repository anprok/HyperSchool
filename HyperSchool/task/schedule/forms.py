from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Student


class SearchForm(forms.Form):
    q = forms.CharField(label='Search', required=False, max_length=32)


class StudentAddForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
