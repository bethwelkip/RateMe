from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as log_in
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from django_registration.forms import RegistrationForm
from .models import Users, Project, Rating, Contact
from .forms import LoginForm, UploadForm
from .accounts import sample
import cloudinary, cloudinary.api,cloudinary.uploader

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
        new_user = Users(name = username, password=make_password(password))
        new_user.contact = contact
        new_user.save()
        return redirect('login')
        #self.cursor.

    return render(request, 'auth/registration_form.html', {"form": form})

def login(request):
    form = AuthenticationForm()
    context = {"form":form}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        attempt_user = Users.objects.filter(name = username).first()
        user = check_password(password, attempt_user.password) if attempt_user is not None else False
        print(make_password(password), attempt_user.password)
        # user = authenticate(request, username=username, password=check_password(password))
        if user:
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
    if len(Project.objects.all())  < 2: 
        sample()
    project = [project for project in Project.objects.all()]
    projects = [(project, [project.ratings]) for project in project] 
    return render(request, 'html/home.html', {'projects': projects})

# @login_required(login_url = 'auth/')
def upload_project(request):
    form = UploadForm()
    if request.method == 'POST':
        image = request.FILES.get('image')
        print(image)
        title = request.POST['title']
        description = request.POST['description'] 
        url = request.POST['url'] 
       
        user = Users.objects.filter(name = 'ussder').first()
        rating = Rating(design = 0, content = 0, usability=0, overall = 0,total_raters = 0)
        rating.save()
        img = cloudinary.uploader.upload_resource(image)
        new_project = Project(title = title,image = img,description = description, url = url, user = user, ratings= rating)
        new_project.save()
        return redirect('home')       

    return render(request, 'html/upload.html', {'form': form})

# @login_required(login_url = 'auth/')
def view_profile(request):
    cur = current_user
    user =  User.objects.filter(id == cur.id)
    contacts = User.objects.filter(user.id == cur.id )
    user_image =user.picture
    user_name = user.name
    projects = Project.objects.filter(user.id == cur.id).all()
    return render(request, 'html/profile.html')

# @login_required(login_url = 'auth/')
def submit_rating(request):
    pass
    
def search_project(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_projects(search_term)
        projects = list()
        for user in searched_projects:
            projects.append(Project.objects.filter(project__id = user.id).first())
        message = f"{search_term}"
        return render(request, 'html/home.html',{"message":message,"projects": projects})

    else:
        message = "You haven't searched for any term \n"
        return render(request, 'search.html',{"message":message})


# Create your views here.
