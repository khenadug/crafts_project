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
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('crafts/', include('crafts.urls')),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='sign_up'),
    path('make_post/', views.make_post, name='make_post'),
    path('login/mypage/', views.user_page, name='my_page'),
    path('login/following/', views.following, name='following'),
    path('login/followers/', views.followers, name='followers'),
    path('login/messages/', views.messages, name='messages'),
    path('userpage/', views.user_page, name='user_page'),
] + static(settings.MEDIA_URL)
