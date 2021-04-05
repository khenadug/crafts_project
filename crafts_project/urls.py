"""crafts_project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from crafts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('crafts/', include('crafts.urls')),
    path('login/', views.user_login, name='login'),
    path('login/mypage/<slug:user_name_slug>/', views.user_page, name='my_page'),
    path('login/following/<slug:user_name_slug>/', views.following, name='following'),
    path('login/followers/<slug:user_name_slug>/', views.followers, name='followers'),
    path('login/messages/<slug:user_name_slug>/', views.messages, name='messages'),
    path('userpage/<slug:user_name_slug>/', views.user_page, name='user_page'),
]