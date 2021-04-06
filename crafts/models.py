from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username

class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images')
    caption = models.CharField(max_length=180)
    tag = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.caption

class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.text

class Message(models.Model):
    recipient = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.text