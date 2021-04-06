from django import forms
from crafts.models import UserProfile, Post, Comment
from django.contrib.auth.models import User
import datetime

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

class PostForm(forms.ModelForm):
    image = forms.FileField(label='Select Image')
    caption = forms.CharField(max_length=180, help_text="Caption")
    tag = forms.CharField(max_length=30, help_text="Tag")
    date = datetime.datetime.now()
    likes = 0
    exclude = ['user',]
    class Meta:
        model = Post
        fields = ('user',)