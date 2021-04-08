from django import forms
from .models import Project, Rating, Users, Contact
from django_registration.forms import RegistrationForm
from urllib import request
class UploadForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['ratings', 'user']

class RegisterForm(forms.Form):
    form = RegistrationForm()

class LoginForm(forms.Form):
    username = forms.CharField()
    # password = forms.PasswordField()
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Users
        exclude = []