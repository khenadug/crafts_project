from django.urls import path
from crafts import views

app_name = 'crafts'

urlpatterns = [
	path('', views.home, name='home'),
    path('login', views.user_login, name='login'),
    path('login/mypage/<slug:user_name_slug>/', views.user_page, name='my_page'),
    path('login/following/<slug:user_name_slug>/', views.following, name='following'),
    path('login/followers/<slug:user_name_slug>/', views.followers, name='followers'),
    path('login/messages/<slug:user_name_slug>/', views.messages, name='messages'),
    path('userpage/<slug:user_name_slug>/', views.user_page, name='user_page'),
]