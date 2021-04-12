from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Contact(models.Model):
    email = models.EmailField(max_length = 100)
    phone = models.CharField(max_length = 100,blank = True, null = True)
    facebook = models.CharField(max_length = 100, blank = True, null = True)
    twitter = models.CharField(max_length = 100, blank = True, null = True)
    linkedIn = models.CharField(max_length = 100, blank = True, null = True)

class Users(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank = True)
    password = models.CharField(max_length = 1000,blank = True)
    picture = CloudinaryField('image', blank = True)
    contact = models.ForeignKey(Contact, blank = True, null = True, on_delete = models.DO_NOTHING)

class Rating(models.Model):
    design = models.IntegerField(blank=True)
    content = models.IntegerField(blank = True)
    usability = models.IntegerField(blank = True)
    overall = models.FloatField(blank = True)
    total_raters = models.IntegerField(blank = True)

class Project(models.Model):
    title = models.CharField(max_length = 100)
    image = CloudinaryField('image', null = True, blank = True)
    description = models.TextField(editable=True, blank = False)
    url = models.CharField(max_length = 100, blank = False, null = False)
    ratings = models.ForeignKey(Rating, on_delete = models.CASCADE)
    user = models.ForeignKey(Users,on_delete = models.CASCADE)

    def search_projects(search):
        projects = Project.objects.all()
        lis = []
        for project in projects:
            if project.description.casefold().__contains__(search.casefold()) or project.title.casefold().__contains__(search):
                lis.append(project)
        return lis


