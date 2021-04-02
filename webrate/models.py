from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Contact(models.Model):
    Email = models.EmailField(max_length = 100)
    Phone = models.CharField(max_length = 100)
    Facebook = models.CharField(max_length = 100, blank = True, null = True)
    Twitter = models.CharField(max_length = 100, blank = True, null = True)
    LinkedIn = models.CharField(max_length = 100, blank = True, null = True)

class User(models.Model):
    Name = models.CharField(max_length=100)
    Picture = CloudinaryField('image', null = True, blank = True)
    Contact = models.ForeignKey(Contact, on_delete = models.DO_NOTHING)

class Ratings(models.Model):
    design = models.IntegerField()
    content = models.IntegerField()
    usability = models.IntegerField()
    overall = models.IntegerField()
    total_raters = models.IntegerField()

class Project(models.Model):
    Title = models.CharField(max_length = 100)
    Image = CloudinaryField('image')
    Description = models.TextField(editable=True, blank = False)
    url = models.CharField(max_length = 100, blank = False, null = False)
    ratings = models.ManyToManyField(Ratings)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

