from django.shortcuts import render, redirect
from django.http import HttpResponse
#from crafts.models import Post, [other Models]
#from crafts.forms import [Forms]
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    post_list = Post.objects.order_by('-likes')[:20]
    
    context_dict = {}
    context_dict['bold message'] = 'crafting your curiosity'
    context_dict['posts'] = post_list
    
    return render(request, 'crafts/home.html', context=context_dict)


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


def following(request, user_name):
    
    return response


def followers(request, user_name):
    
    return response


def messages(request, user_name):
    
    return response


def user_page(request, user_name):
    
    return response
