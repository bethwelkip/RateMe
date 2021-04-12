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
        include = ['HomeTown']
        exclude = ['contact', 'password']
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = []

class RatingForm(forms.Form):
    choices = (
    ("1", 1),
    ("2", 2),
    ("3",3),
    ("4", 4),
    ("5", 5),
    ("6", 6),
    ("7", 7),
    ("8", 8),
    ("9", 9),
    ("10", 10),
)
    design = forms.ChoiceField(choices=choices)
    content = forms.ChoiceField(choices=choices)
    usability = forms.ChoiceField(choices=choices)