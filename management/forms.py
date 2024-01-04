from django import forms
from django.forms import ModelForm
from . models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

        widgets = {
        'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name', 'class' : "form-control"}),
        'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name', 'class' : "form-control"}),
        'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class' : "form-control"}),
        'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class' : "form-control"}),
        'phone_no': forms.TextInput(attrs={'placeholder': 'Enter your phone number', 'class' : "form-control"}),
        'gender': forms.Select(attrs={'class' : "form-control"}, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]),
    }