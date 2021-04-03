from django import forms
from .models import Project, Rating, User, Contact
from django_registration.forms import RegistrationForm
from urllib import request
class UploadForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['likes','comments', 'profile','pub_date']

class RegisterForm(forms.Form):
    form = RegistrationForm()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ["user", "following"]