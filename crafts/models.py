from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #user_name = models.CharField(max_length=30, unique=True)
    #password = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='user_picture', blank=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username

class Post(models.Model):
    image = models.ImageField(upload_to='post_images', blank=True)
    caption = models.CharField(max_length=180)
    tag = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.caption

class Comment(models.Model):
    text = models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.text

class Message(models.Model):
    recipient = models.CharField(max_length=30)
    text = models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.text