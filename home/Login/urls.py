from django.urls import path
from Login import views
from django.contrib.auth import views as auth_views  #logout



urlpatterns = [
    path('login/', views.home),
    path('register/', views.register_page, name='register_page'),
    path('', views.register_page, name='register_page'),
    path('login/', views.login_page, name='login_page'),
    #logout lai function call garesi pughyo 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]