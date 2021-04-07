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
    picture = CloudinaryField('image', null = True, blank = True)
    contact = models.ForeignKey(Contact, on_delete = models.DO_NOTHING)

class Rating(models.Model):
    design = models.IntegerField()
    content = models.IntegerField()
    usability = models.IntegerField()
    overall = models.IntegerField()
    total_raters = models.IntegerField()

class Project(models.Model):
    title = models.CharField(max_length = 100)
    image = CloudinaryField('image')
    description = models.TextField(editable=True, blank = False)
    url = models.CharField(max_length = 100, blank = False, null = False)
    ratings = models.ManyToManyField(Rating)
    user = models.ForeignKey(Users, on_delete = models.CASCADE)

