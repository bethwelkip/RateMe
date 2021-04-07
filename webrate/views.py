from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as log_in
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django_registration.forms import RegistrationForm
from .models import Users, Project, Rating, Contact

def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, email = email, password = password)
        user.save()
        contact = Contact(email = email)
        contact.save()
        new_user = Users(name = username)
        new_user.contact = contact
        new_user.save()
        return redirect('login')
        #self.cursor.

    return render(request, 'auth/registration_form.html', {"form": form})

def login(request):
    form = AuthenticationForm()
    context = {"form":form}
    users = User.objects.all()
    print([(user.username, user.password) for user in users])
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password = password)
        print(user)
        if user is not None:
            log_in(request, user)
            return redirect('view_profile')
        else: 
            messages.info(request, "Username or Password is incorrect")
            context.update({"messages": messages})
            return redirect('login')

    return render(request, 'auth/login_form.html', context)

def logout_me(request):
    logout(request)
    messages.info(request, "You have logged out successfully!")
    return redirect("login")

def home(request):
    register = " HI "
    return render(request, 'html/home.html')

# @login_required(login_url = 'auth/')
def upload_project(request):

    return render(request, 'html/upload.html')

# @login_required(login_url = 'auth/')
def view_profile(request):
    cur = current_user
    user =  User.objects.filter(id == cur.id)
    contacts = User.objects.filter(user.id == cur.id )
    user_image =user.picture
    user_name = user.name
    projects = Project.objects.filter(user.id == cur.id).all()
    return render(request, 'html/profile.html')

@login_required(login_url = 'auth/')
def submit_rating(request):
    pass
    
def search_project(request):
    pass


# Create your views here.
