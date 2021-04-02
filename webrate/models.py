from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=100)
    Picture = CloudinaryField('image', null = True, blank = True)
    Projects = models.ManyToManyField()
    Contact = models.ForeignKey(Contact, on_delete = models.DO_NOTHING)
class Contact(models.Model):
    Email = models.EmailField()
    Phone = models.CharField()
    Facebook = models.CharField(blank = True, null = True)
    Twitter = models.CharField(blank = True, null = True)
    LinkedIn = models.CharField(blank = True, null = True)
class Project(models.Model):
    Title = models.CharField(max_length = 100)
    Image = models.ImageField()
    Description = models.TextField(editable=True, blank = False)
    url = models.CharField(blank = False, null = False)
    ratings = Models.ManyToManyField(Ratings)
class Ratings(models.Model):
    design = models.IntegerField()
    content = models.IntegerField()
    usability = models.IntegerField()
    overall = models.IntegerField()
    total_raters = models.IntegerField()
