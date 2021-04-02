from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def  register(request):
    pass
def login(request):
    pass

def home(request):
    return render(request, 'html/base.html' )

@login_required(login_url = 'auth/')
def upload_project(request):
    pass

@login_required(login_url = 'auth/')
def view_profile(request):
    pass

@login_required(login_url = 'auth/')
def submit_rating(request):
    pass
    
def search_project(request):
    pass


# Create your views here.
