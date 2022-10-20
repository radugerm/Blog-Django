from distutils.command.upload import upload
from email.mime import image
from msilib.schema import Class
from turtle import title, width
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import ImageField


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length= 50)
    email = models.EmailField()
    mesaj = models.TextField(max_length=800)
    
    
class Video (models.Model):
    caption= models.CharField(max_length= 200,default='SOME STRING')
    video = models.FileField(upload_to = 'forever/videos/%y')    
    def __str__(self):
        return self.caption
    
class Image(models.Model):
          
    image = models.ImageField(upload_to= "forever/pictures/%y")
    caption = models.TextField() 
    def __str__(self):
        return self.caption

class About(models.Model):
    image = models.ImageField(upload_to = "forever/about_me/%y")
    caption = models.TextField()
    def __str__(self):
        return self.caption
    
class Homee(models.Model):
    title = models.CharField(max_length=140, default='SOME STRING')
    image = models.ImageField(upload_to= "forever/home/%y")
    caption = models.TextField()
    
    
    def __str__ (self):
        return self.caption 
    
    
