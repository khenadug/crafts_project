from django.shortcuts import render, redirect
from django.http import HttpResponse
from crafts.models import UserProfile, Post, Comment, Message
from crafts.forms import UserForm, UserProfileForm, PostForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    post_list = Post.objects.order_by('-likes')[:20]
    
    context_dict = {}
    context_dict['posts'] = post_list
    
    return render(request, 'crafts/home.html', context=context_dict)


def following(request, user_name):
    user_list = UserProfile.objects.order_by('-User.username')
    
    context_dict = {}
    context_dict['following_list'] = user_list
    
    return render(request, 'crafts/following.html', context=context_dict)


def followers(request, user_name):
    user_list = UserProfile.objects.order_by('-User.username')
    
    context_dict = {}
    context_dict['followers_list'] = user_list
    
    return render(request, 'crafts/followers.html', context=context_dict)


def messages(request, user_name):
    
    return response


def user_page(request, user_name):
    post_list = Post.objects.get(user.UserProfile.username==user_name)
    context_dict = {}
    context_dict['posts'] = post_list
    return render(request, 'crafts/userpage.html', context=context_dict)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            return redirect(reverse('crafts:home'))
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'crafts/login.html')


def user_signup(request):
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 
                'crafts/signup.html', 
                context = {'user_form': user_form,
                            'profile_form': profile_form,
                            'registered': registered})


def make_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) #user=request.user
        if form.is_valid():
            newPost = Post(user = request.user, image = request.FILES['image'])
            newPost.save(commit=True)
            return redirect('/crafts/')
        else:
            print(form.errors)
    return render(request, 'crafts/make_post.html', {'form': form})