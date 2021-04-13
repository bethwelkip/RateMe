from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as log_in
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from django_registration.forms import RegistrationForm
from .models import Users, Project, Rating, Contact
from .forms import LoginForm, UploadForm, RatingForm, UpdateForm, ContactForm
import cloudinary, cloudinary.api,cloudinary.uploader
from werkzeug.security import generate_password_hash,check_password_hash

def register(request):
    form = UserCreationForm()#RegistrationForm(data=request.POST)
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            new_user = Users(name = user.username)
            new_user.save()
            # log_in(request, user)
            # user= form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            # password = form.cleaned_data.get('password')
            # user = User.objects.create_user(username=user, email=email, password=password)
            # print(user, password)
            # contact = Contact(email = email)
            # contact.save()
            # new_user = Users(name = user, password=user.password)
            # new_user.contact = contact
            # new_user.save()
            return redirect('login')
            #CompressedManifestStaticFilesStorage20
    return render(request, 'auth/registration_form.html', {"form": form})

def login(request):
    form = AuthenticationForm(data=request.POST)
    context = {"form":form}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            log_in(request, user)
            return redirect('home')
    else: 
        # messages.info(request, "Username or Password is incorrect")
        # context.update({"messages": messages})
        # return redirect('login')
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

@login_required(login_url = 'auth/')
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
def submit_rating(request, id):
    ied = id
    state = True
    form = RatingForm()
    rated_project = Project.objects.filter(id = int(ied)).first()
    if form.is_valid() or request.method == 'POST':
        usab = int(request.POST['usability'])
        cont = int(request.POST['content'])
        des = int(request.POST['design'])
        current_usab = (rated_project.ratings.usability)*(rated_project.ratings.total_raters) + usab
        current_cont = rated_project.ratings.content*(rated_project.ratings.total_raters) + cont
        current_des = rated_project.ratings.design*(rated_project.ratings.total_raters) + des
        total_raters = rated_project.ratings.total_raters + 1
        rated_project.ratings.total_raters = total_raters
        rated_project.ratings.design = round(current_des/total_raters, 2)
        rated_project.ratings.content =  round(current_cont/total_raters, 2)
        rated_project.ratings.usability = round(current_usab/total_raters, 2)
        rated_project.ratings.overall = round((rated_project.ratings.design + rated_project.ratings.content  + rated_project.ratings.usability )/(3), 2)
        rated_project.ratings.save()
        rated_project.save()
        project = [project for project in Project.objects.all()]
        projects = [(project, [project.ratings],True if project.id == int(ied) else False) for project in project] 
        return redirect('view_project', id = ied)
    project = [project for project in Project.objects.all()]
    projects = [(project, [project.ratings],True if project.id == int(ied) else False) for project in project] 
    return render(request, 'html/image.html',{"state": state,"form":form, "project": rated_project})
    
def search_project(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_projects(search_term)
        projects = list()
        for project in searched_projects:
            projects.append((project, [project.ratings], project.id))
        message = f"You have searched for {search_term}"
        return render(request, 'html/home.html',{"message":message,"projects": projects})

    else:
        return redirect('home')
def view_project(request, id):
    rated_project = Project.objects.filter(id = int(id)).first()
    state = False
    return render(request, 'html/image.html', {"project": rated_project,"button": state})
def update_profile(request):
    if request.method == 'POST':
        update_form = UpdateForm(data = request.POST)
        contact_form = ContactForm(data = request.POST)
        print("GGGGGGGG")
        if update_form.is_valid() and contact_form.is_valid():
            user = update_form.save()
            # print(user)
            contact = contact_form.save()
            print(contact)
            # user.contact = contact
            # user.save()
            return redirect('home')
    else:
        update_form = UpdateForm()
        contact_form = ContactForm()
        return render(request, 'html/profile_form.html', {"update_form":update_form, "contact_form":contact_form  })


# Create your views here.
